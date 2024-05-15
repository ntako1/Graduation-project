import serial
import time

def read_from_arduino():
    ser = serial.Serial('COM3', 9600, timeout=0)
    while True:
        try:
            time.sleep(120)  # sleep for a full second before next read
            data = ser.readline().decode('utf-8').strip()  # read data from the serial port
            if data:
                return data.split(',')  # assuming your data from Arduino comes comma-separated
        except serial.SerialException as e:
            print(f"Error reading from serial port: {str(e)}")
            return None
        except TypeError as e:
            print(f"Type error: {str(e)}")
            return None
