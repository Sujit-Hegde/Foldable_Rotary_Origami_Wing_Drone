# Foldable Rotary Origami Wing (FROW) Drone

A bio-inspired **Foldable Rotary Origami Wing (FROW) Drone** that combines the energy efficiency of a **monocopter** with an **origami-inspired morphing wing mechanism**. The drone actively changes its wingspan during operation using a servo-driven folding mechanism, enabling it to transition between efficient hovering and compact flight configurations suitable for navigating confined environments.

This project was developed as a **Bachelor of Engineering Final Year Project** in the Department of Electronics and Instrumentation Engineering, **Sri Jayachamarajendra College of Engineering (SJCE), JSS Science and Technology University, Mysuru**.

---

# Project Overview

Conventional quadcopters have a fixed geometry that limits their ability to fly through narrow passages such as pipelines, collapsed structures, and confined industrial environments.

The **Foldable Rotary Origami Wing (FROW) Drone** addresses this limitation by integrating an accordion-style origami wing capable of reducing its wingspan during operation. The platform adopts a **single-actuator monocopter configuration**, producing lift through a rotating wing while maintaining a lightweight and energy-efficient design.

The project combines:

- Bio-inspired aerodynamics
- Origami engineering
- Embedded control
- Wireless web-based control
- Mechanical morphing
- Raspberry Pi Pico W based control

---

# Features

- Active origami wing folding mechanism
- Approximately **40% wingspan reduction**
- Lightweight monocopter platform
- Raspberry Pi Pico W based controller
- Brushless DC motor propulsion
- Servo-controlled folding mechanism
- Wireless control through Wi-Fi
- React.js based dashboard
- Node.js backend server
- Adjustable motor pulse width
- Adjustable motor hold time
- Safe motor ramp-up and ramp-down sequence
- Remote operation through browser

---

# Project Demonstration

The complete web dashboard is deployed on **Vercel**.

### Live Website

https://trial-web-snowy.vercel.app

The dashboard allows users to:

- Turn system ON/OFF
- Fold the wings
- Reset the wings
- Configure maximum ESC pulse
- Configure motor hold time
- Send commands wirelessly to Raspberry Pi Pico W

---

# Repository Structure

```
Foldable_Rotary_Origami_Wing_Drone/
│
├── 3D Design/
│   ├── Servo Holder
│   ├── Wing Holder
│   ├── Guide Track
│   ├── Motor Mount
│   ├── Wing Hanger
│
├── backend/
│   ├── server.js
│   ├── package.json
│   ├── package-lock.json
│   └── .gitignore
│
├── trial-web/
│   ├── public/
│   ├── scripts/
│   ├── src/
│   ├── package.json
│   ├── package-lock.json
│   ├── README.md
│   └── .gitignore
│
├── main.py
│
├── FROW Report.pdf
│
└── README.md
```

---

# Repository Description

## 3D Design

This folder contains all CAD models and 3D printable structural components used in the drone.

The components include:

- Servo Holder
- Wing Holder
- Wing Hanger Supports
- Slider Mechanism
- Guide Track Endcaps
- Motor Holders
- Structural Mounts

These parts were designed to assemble the foldable origami wing mechanism while maintaining structural rigidity during high-speed rotation.

---

## backend

The backend is developed using **Node.js** and serves as the communication bridge between the web dashboard and the Raspberry Pi Pico W.

Functions include:

- Store current drone state
- Receive dashboard commands
- Provide REST API endpoints
- Synchronize motor commands
- Synchronize servo commands

Main file:

```
server.js
```

---

## trial-web

This folder contains the complete frontend application developed using **React.js**.

The dashboard provides:

- Power Toggle
- Fold Button
- Reset Button
- Hold Time Input
- Maximum Pulse Input
- Real-time communication with backend

The frontend is deployed on:

https://trial-web-snowy.vercel.app

---

## main.py

This file contains the **entire Python program executed on the Raspberry Pi Pico W**.

Unlike traditional embedded projects, **no firmware development framework is used**.

The Raspberry Pi Pico W directly executes this Python program to:

- Connect to Wi-Fi
- Read dashboard commands
- Control ESC
- Control Servo Motors
- Execute safe motor ramping
- Execute folding sequence
- Update backend state

Major functionalities include:

- Wi-Fi communication
- HTTP REST requests
- PWM generation
- Servo control
- ESC control
- Safety limits
- Motor ramp-up
- Motor ramp-down
- Automatic backend synchronization

---

## FROW Report.pdf

This document contains the complete technical documentation of the project.

The report describes every stage of development, from concept to prototype testing, including theoretical background, hardware implementation, software architecture, experimental results, and future improvements.

### Contents of the Report

### Chapter 1 – Introduction

Introduces the motivation behind the project, discusses the limitations of conventional UAVs, presents the concept of the Foldable Rotary Origami Wing (FROW) Drone, and explains the objectives, project overview, and report organization.

---

### Chapter 2 – Literature Review

Presents a comprehensive survey of research papers related to:

- Monocopters
- Bio-inspired UAVs
- Morphing drones
- Origami engineering
- Foldable aerial robots

The chapter also compares existing systems, identifies their limitations, and explains how the proposed FROW drone addresses these challenges.

---

### Chapter 3 – Methodology

Describes the complete design methodology of the project, including:

- Project objectives
- Bio-inspired aerodynamic concepts
- Origami engineering principles
- Rotating platform control theory
- System architecture
- Hardware block diagram
- Circuit diagram
- Prototype design
- Performance evaluation metrics

---

### Chapter 4 – Hardware Description

Explains the physical implementation of the drone.

Topics covered include:

- Design specifications
- Material selection
- 3D printed components
- Servo holder
- Wing hanger supports
- Motor mounts
- Guide track endcaps
- Wing holder
- Fabrication parameters
- Hardware integration

This chapter describes the complete construction and assembly of the FROW prototype.

---

### Chapter 5 – Software Description

Describes the complete software architecture of the system.

It includes:

- Dashboard implementation
- User Interface
- Backend communication
- Python control program
- Control logic
- Safety mechanisms
- Wireless communication
- System workflow

The software enables real-time wireless control of the drone through a web browser.

---

### Chapter 6 – Results and Discussion

Presents the experimental evaluation of the developed prototype.

The chapter discusses:

- Ground testing
- Lift-off experiments
- Folding mechanism performance
- Mechanical observations
- Rotational behavior
- Experimental results
- Performance analysis

The obtained results validate the effectiveness of the foldable monocopter concept.

---

### Chapter 7 – Conclusion and Future Work

Summarizes the overall achievements of the project.

This chapter discusses:

- Project conclusions
- Advantages
- Current limitations
- Practical applications
- Future enhancements

Potential future improvements include autonomous navigation, obstacle detection, advanced stabilization algorithms, and improved flight control.

---

The report also contains:

- Abstract
- Acknowledgements
- List of Figures
- List of Tables
- List of Abbreviations
- References
- Appendix

---

# Hardware Used

- Raspberry Pi Pico W - https://robu.in/product/raspberry-pi-pico-w/
- Brushless DC Motor - https://robu.in/product/flywoo-co-brand-nin-1404-v2-dave-c-fpv-fpv-motortitan-4850kv/
- Electronic Speed Controller (ESC) - https://robu.in/product/30a-bldc-esc-electronic-speed-controller/
- Servo Motor - https://robu.in/product/towerpro-sg90-continuous-rotation-360-degree-servo-motor/
- Li-Po Battery - https://robu.in/product/orange-11-1v-1500mah-3s-40c-lipo-battery-pack-xt60-connector/
- Carbon Fiber Rods - https://robu.in/product/pultruded-square-carbon-hollow-fiber-tube-22mmod-1mmid-400mml-2pcs/
- Balsa Wood - https://www.rcdhamaka.com/product/balsa-sheet-2mm-x-100mm-x-1000mm/
- Polymer Lamination Film - https://www.flightmode.co.in/products/transparent-clear-covering-film-1-meter

---

# Software Used

Frontend

- React.js

Backend

- Node.js
- Express.js

Controller

- Python (Raspberry Pi Pico W)

Communication

- HTTP REST API
- JSON

Development Tools

- Thonny (For Python coding)
- Visual Studio Code

---

# Working Principle

1. User opens the web dashboard.
2. Commands are sent to the backend server.
3. Raspberry Pi Pico W periodically fetches the current state.
4. Python program interprets received commands.
5. Servo motors fold or unfold the origami wings.
6. ESC generates PWM signals to control the BLDC motor.
7. Motor speed gradually increases and decreases for safe operation.
8. Backend updates the current drone status.

---

# Future Improvements

- Closed-loop flight stabilization
- IMU integration
- PID-based control
- LiDAR obstacle detection
- Camera-based navigation
- Autonomous flight
- Waypoint navigation
- UDP communication
- Telemetry support
- Mobile application
- Flight data logging

---

# Authors

**Sujit Satish Hegde**

Department of Electronics and Instrumentation Engineering

Sri Jayachamarajendra College of Engineering

JSS Science and Technology University

---

**Virupaksha A. Alur**

Department of Electronics and Instrumentation Engineering

Sri Jayachamarajendra College of Engineering

JSS Science and Technology University

---

**Abhishek K. T**

Department of Electronics and Instrumentation Engineering

Sri Jayachamarajendra College of Engineering

JSS Science and Technology University

---


# License

This repository is intended for **academic and educational purposes**.

Feel free to use the project for learning and research while providing appropriate credit to the authors.

---

⭐ If you found this project useful, consider giving this repository a star.
