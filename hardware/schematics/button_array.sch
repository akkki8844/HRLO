TITLE: HRLO Button Array Schematic

COMPONENTS:
- Microcontroller: ESP32 Dev Module
- Buttons: 5 × Momentary Push Buttons (Normally Open)
- Power: USB (5V → onboard 3.3V regulation)
- Ground: Common GND rail

CONNECTIONS:

BUTTON 1:
- One terminal → GPIO12 (ESP32)
- Other terminal → GND

BUTTON 2:
- One terminal → GPIO14 (ESP32)
- Other terminal → GND

BUTTON 3:
- One terminal → GPIO27 (ESP32)
- Other terminal → GND

BUTTON 4:
- One terminal → GPIO26 (ESP32)
- Other terminal → GND

BUTTON 5:
- One terminal → GPIO25 (ESP32)
- Other terminal → GND

LOGIC CONFIGURATION:
- GPIO pins configured as INPUT_PULLUP
- Default state: HIGH
- Button press: LOW

DEBOUNCE:
- Implemented in firmware (50 ms)
- No external capacitors required

GROUNDING:
- All button ground terminals connected to a single GND rail
- ESP32 GND connected to same rail

NOTES:
- No external resistors required
- Avoid long wires to reduce noise
- Do not connect buttons to 5V or 3.3V directly
- ESP32 internal pull-ups provide stable logic levels

END SCHEMATIC
