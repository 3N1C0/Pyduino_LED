import serial
import serial.tools.list_ports

# List all available ports
ports = serial.tools.list_ports.comports()
portsList = []

print("Available Serial Ports:")
for i, port in enumerate(ports):
    portsList.append(port.device)
    print(f"[{i}] {port.device} - {port.description}")

# Ask the user to choose a port by index
index = int(input("Select the port index for your Arduino: "))
use = portsList[index]

# Configure and open the serial connection
serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()

print(f"Connected to {use}")


while True:
    command = input("Arduino Command (ON/OFF/exit): ")
    serialInst.write(command.encode('utf-8'))

    if command == 'exit':
        quit()