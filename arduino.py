import serial
import time

class ServoController:
    def __init__(self, port='COM3', baudrate=9600):
        self.arduino = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # Allow time for Arduino to initialize
        
    def set_position(self, horizontal, vertical):
        """Set servo positions (0-180 degrees)"""
        if not (0 <= horizontal <= 180) or not (0 <= vertical <= 180):
            raise ValueError("Position values must be between 0 and 180")
            
        command = f"{horizontal},{vertical}\n"
        self.arduino.write(command.encode())
        
    def center(self):
        """Center both servos"""
        self.set_position(90, 90)
        
    def close(self):
        """Close serial connection"""
        self.arduino.close()

# Example usage
if __name__ == "__main__":
    # Update COM port to match your Arduino
    controller = ServoController(port='COM5')
    
    try:
        # Center servos
        controller.center()
        time.sleep(1)
        
        # Move to different positions
        controller.set_position(45, 135)  # Left-Up
        time.sleep(1)
        controller.set_position(135, 45)  # Right-Down
        time.sleep(1)
        controller.center()
        
    finally:
        controller.close()