# import time
# import board
# import busio
# from adafruit_ads1x15.analog_in import AnalogIn
# import adafruit_ads1x15.ads1115 as ADS
# import os

# file_path = '/home/aptech/Desktop/projects/myenv/voltage.py'
# if os.path.exists(file_path):
#     with open(file_path, 'r') as f:
#         # Process your file here
#         pass
# else:
#     print(f"File not found: {file_path}")
# # Create the I2C bus
# i2c = busio.I2C(board.SCL, board.SDA)

# # Create the ADS object
# ads = ADS.ADS1115(i2c)

# # Set the gain (this depends on the expected input voltage range from the current sensor)
# ads.gain = 1

# R1 = 10000  # 10kΩ
# R2 = 2200   # 2.2kΩ
# V_in = 12  

# # Create a single-ended input on channel 1 (A1) for voltage reading
# chan = AnalogIn(ads, ADS.P1)

# def read_voltage():
#     # Read the voltage from the sensor
#     voltage = chan.voltage
#     # Calculate the actual voltage based on the divider
#     actual_voltage = voltage * (R1 + R2) / R2
#     return actual_voltage

# # Continuously read and print the voltage
# try:
#     while True:
#         voltage = read_voltage()
#         print(f"Voltage: {voltage:.3f} V")
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("Script stopped")
















import time
import board
import busio
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS
import os

file_path = '/home/aptech/Desktop/projects/myenv/voltage.py'
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        # Process your file here
        pass
else:
    print(f"File not found: {file_path}")
# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADS object
ads = ADS.ADS1115(i2c)

# Set the gain (this depends on the expected input voltage range from the current sensor)
ads.gain = 1

R1 = 10000  # 10kΩ
R2 = 2200   # 2.2kΩ
V_in = 12  

# Create a single-ended input on channel 1 (A1) for voltage reading
chan = AnalogIn(ads, ADS.P1)

def read_voltage():
    # Read the voltage from the sensor
    voltage = chan.voltage
    # Calculate the actual voltage based on the divider
    actual_voltage = voltage * (R1 + R2) / R2
    return actual_voltage

if __name__ == "__main__":
    # Continuously read and print the voltage
    try:
        while True:
            voltage = read_voltage()
            print(f"Voltage: {voltage:.3f} V")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Script stopped")