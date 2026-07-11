import network
import urequests
import time
import gc
import ujson
from machine import Pin, PWM

# ---------------- WIFI ----------------
ssid = "YOUR_WIFI_SSID"
password = "YOUR_WIFI_PASSWORD"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    print("Connecting...")
    time.sleep(1)

print("Connected:", wlan.ifconfig())

BASE_URL = "https://trial-web-1.onrender.com"

# ---------------- PWM SETUP ----------------
servo1 = PWM(Pin(14))
servo2 = PWM(Pin(15))
esc = PWM(Pin(16))

for p in (servo1, servo2, esc):
    p.freq(50)


def set_pulse(pwm, pulse_ms):
    duty = int((pulse_ms / 20) * 65535)
    pwm.duty_u16(duty)


# ---------------- INITIAL ----------------
set_pulse(esc, 1.0)
time.sleep(3)

# ---------------- FLAGS ----------------
motor_running = False
servo_done = False

# ---------------- MAIN LOOP ----------------
while True:
    try:
        res = urequests.get(BASE_URL + "/state")
        text = res.text
        res.close()

        data = ujson.loads(text)

        power = data.get("power")
        servo_cmd = data.get("servo")

        motor_data = data.get("motor", {})
        motor_power = motor_data.get("power")
        hold_time = motor_data.get("holdTime", 0)
        max_pulse = motor_data.get("maxPulse", 1.05)

        # -------- SAFETY CLAMP --------
        if max_pulse > 1.5:
            max_pulse = 1.5

        if max_pulse < 1.1:
            max_pulse = 1.1

        # -------- POWER OFF --------
        if power == "OFF":
            print("Power OFF")

            set_pulse(esc, 1.0)

            motor_running = False
            servo_done = False

            time.sleep(1)
            continue

        # -------- POWER ON --------
        if power == "ON":

            # -------- SERVO --------
            if servo_cmd == "FOLD" and not servo_done:
                print("Servo folding...")

                set_pulse(servo1, 1.3)
                set_pulse(servo2, 1.3)

                time.sleep(3.8)

                set_pulse(servo1, 1.5)
                set_pulse(servo2, 1.5)

                servo_done = True

                try:
                    r = urequests.post(BASE_URL + "/reset-servo")
                    r.close()
                except:
                    pass

            # -------- MOTOR --------
            if motor_power == "ON" and not motor_running:

                print("Motor START")
                print("Max Pulse:", max_pulse)

                motor_running = True

                # -------- RAMP UP --------
                val = 1.0

                while val <= max_pulse:
                    set_pulse(esc, round(val, 2))
                    val += 0.05
                    time.sleep(0.5)

                # -------- HOLD --------
                print("Holding for", hold_time)

                set_pulse(esc, max_pulse)
                time.sleep(hold_time)

                # -------- RAMP DOWN --------
                val = max_pulse

                while val >= 1.0:
                    set_pulse(esc, round(val, 2))
                    val -= 0.05
                    time.sleep(0.5)

                set_pulse(esc, 1.0)

                motor_running = False

                # -------- UPDATE BACKEND --------
                try:
                    r = urequests.post(
                        BASE_URL + "/motor",
                        headers={"Content-Type": "application/json"},
                        data=ujson.dumps({
                            "power": "OFF",
                            "holdTime": hold_time,
                            "maxPulse": max_pulse
                        })
                    )

                    r.close()

                    print("Motor OFF updated")

                except Exception as e:
                    print("Backend error:", e)

        gc.collect()
        time.sleep(0.5)

    except Exception as e:
        print("Error:", e)
        gc.collect()
        time.sleep(2)