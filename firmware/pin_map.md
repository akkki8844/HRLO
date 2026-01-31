# ESP32 Button Array Pin Map — HRLO

## Overview
This document defines the physical wiring between the ESP32 microcontroller and the button array used for step-wise reasoning capture in HRLO. Each button corresponds to a single reasoning step marker.

---

## Microcontroller
- Board: ESP32 Dev Module
- Logic level: 3.3V
- Input mode: Internal pull-up resistors

---

## Button Wiring Principle
- One terminal of each button connects to **GND**
- The other terminal connects to a GPIO pin
- Buttons are configured as `INPUT_PULLUP`
- Button press pulls the pin **LOW**

No external resistors are required.

---

## Pin Assignments

| Button Number | GPIO Pin | Function |
|--------------|----------|----------|
| Button 1 | GPIO 12 | Step marker 1 |
| Button 2 | GPIO 14 | Step marker 2 |
| Button 3 | GPIO 27 | Step marker 3 |
| Button 4 | GPIO 26 | Step marker 4 |
| Button 5 | GPIO 25 | Step marker 5 |

---

## Ground Connections
- All buttons share a common **GND**
- Use a breadboard ground rail if available

---

## Electrical Notes
- GPIOs chosen avoid strapping pins
- Internal pull-ups reduce noise
- Debounce handled in firmware
- Keep wires short to minimize interference

---

## Safety and Reliability
- Do not connect buttons to 5V
- Ensure ESP32 is powered via USB only
- Verify continuity before powering on

---

## Verification Checklist
- Board selected as ESP32 Dev Module
- Correct COM port selected
- Serial baud rate set to 115200
- Each button press prints `BUTTON,<n>` to Serial Monitor

---

## Troubleshooting
- If buttons trigger without pressing: check ground wiring
- If no output: verify pull-up configuration
- If multiple triggers: increase debounce delay

This pin map must remain consistent with `esp32_latency_capture.ino`.
