# Pyduino LED

A Python script that turns an LED on and off through an Arduino Uno. You type a command in the terminal, and Python sends it over USB serial.

Based on LeMaster Tech's video on controlling an Arduino from Python. The original video used Windows; this version was written for macOS: [video link](https://youtu.be/UeybhVFqoeg?si=XRiEzKHIn_XHsUEy).

## Files

| File | What it is |
|---|---|
| `Pyduino_LED.py` | Python: lists serial ports, opens the Arduino, and sends typed commands |
| `Arduino_Uno_Setup` | The Arduino sketch (despite the name, it is code, not a setup guide) |
| `Arduino_Circuit_Updated.png` | Circuit diagram |

## Skills demonstrated

- **Serial communication** with `pyserial`.
- **Command-line interaction:** listing devices, letting the user choose one, and handling input.
- **Hardware basics:** wiring an LED and a resistor to an Arduino Uno.

## Run it

1. Upload `Arduino_Uno_Setup` to the Arduino Uno. Wire the red LED to pin 2 and the blue LED to pin 3, each through a resistor (see `Arduino_Circuit_Updated.png`).
2. Install the library: `pip install pyserial`.
3. Run `python Pyduino_LED.py`, choose the Arduino's port, then type a command:
   - `ON` turns the red LED on
   - `OFF` turns the red LED off
   - anything else makes the blue LED blink five times
   - `exit` quits the script
