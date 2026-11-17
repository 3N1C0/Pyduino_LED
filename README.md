# Pyduino LED

A Python script that turns an LED on and off through an Arduino Uno. You type a command in the terminal, and Python sends it over USB serial.

Based on LeMaster Tech's video on controlling an Arduino from Python. The original video used Windows; this version was written for macOS: [video link](https://youtu.be/UeybhVFqoeg?si=XRiEzKHIn_XHsUEy).

## Files

| File | What it is |
|---|---|
| `Pyduino_LED.py` | Python: lists serial ports, opens the Arduino, and sends typed commands |
| `Arduino_Uno_Setup` | Wiring image |
| `Arduino_Circuit_Updated.png` | Circuit diagram |

## Skills demonstrated

- **Serial communication** with `pyserial`.
- **Command-line interaction:** listing devices, letting the user choose one, and handling input.
- **Hardware basics:** wiring an LED and a resistor to an Arduino Uno.

## Run it

1. Upload a sketch to the Arduino that reads serial input and switches the LED on pin 13 for `ON` and off for `OFF`.
2. Install the library: `pip install pyserial`.
3. Run `python Pyduino_LED.py`, choose the Arduino's port, then type `ON`, `OFF`, or `exit`.
