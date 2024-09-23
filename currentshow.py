# import time
# import board
# import busio
# from adafruit_ads1x15.analog_in import AnalogIn
# import adafruit_ads1x15.ads1115 as ADS


# # Create the I2C bus
# i2c = busio.I2C(board.SCL, board.SDA)

# # Create the ADS object
# ads = ADS.ADS1115(i2c)

# # Set the gain (this depends on the expected input voltage range from the current sensor)
# ads.gain = 1

# # Create a single-ended input on channel 0 (A0)
# chan = AnalogIn(ads, ADS.P1)

# # ACS712 has a reference voltage at 2.5V, so to get the current, we need to
# # subtract the reference voltage from the reading and then convert to current
# # based on the sensitivity (e.g., 185mV/A for ACS712-5A)

# REFERENCE_VOLTAGE = 2.5  # Midpoint of the ACS712 output at 0A
# SENSITIVITY = 0.185  # Sensitivity in V/A (for ACS712-5A version)

# def read_current():
#     # Read the voltage from the sensor
#     voltage = chan.voltage
#     # Calculate the current based on the sensitivity
#     current = (voltage - REFERENCE_VOLTAGE) / SENSITIVITY
#     return current

# # Continuously read and print the current
# try:
#     while True:
#         current = read_current()
#         print(f"Current: {current:.3f} A")
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("Script stopped")


# import time
# import board
# import busio
# from adafruit_ads1x15.analog_in import AnalogIn
# import adafruit_ads1x15.ads1115 as ADS

# # Set up I2C and ADS1115
# i2c = busio.I2C(board.SCL, board.SDA)
# ads = ADS.ADS1115(i2c)
# chan = AnalogIn(ads, ADS.P0)


# R1 = 10000  # 10kΩ
# R2 = 2200   # 2.2kΩ
# V_in = 12  


# def read_current():
#     voltage = chan.voltage  # Read voltage from the ADC
#     actual_voltage = voltage * (R1 + R2) / R2

#     print(f"Raw Voltage: {actual_voltage:.3f} V")
#     current = (voltage - 2.5) / 0.185  # Adjust based on sensor sensitivity
#     return current

# try:
#     while True:
#         current = read_current()
#         print(f"Current: {current:.3f} A")
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("Script stopped")



# import time
# import board
# import busio
# from adafruit_ads1x15.analog_in import AnalogIn
# import adafruit_ads1x15.ads1115 as ADS

# # Set up I2C and ADS1115
# i2c = busio.I2C(board.SCL, board.SDA)
# ads = ADS.ADS1115(i2c)
# chan = AnalogIn(ads, ADS.P0)

# R1 = 10000  # 10kΩ
# R2 = 2200   # 2.2kΩ

# def read_current():
#     voltage = chan.voltage  # Read voltage from the ADC
#     actual_voltage = voltage * (R1 + R2) / R2  # Adjust for voltage divider
#     print(f"Raw Voltage: {actual_voltage:.3f} V")
    
#     # Calculate current based on the actual voltage
#     current = (actual_voltage - 2.5) / 0.185  # Use actual_voltage here
#     return current

# try:
#     while True:
#         current = read_current()
#         print(f"Current: {current:.3f} A")
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("Script stopped")


# import time
# import board
# import busio
# from adafruit_ads1x15.analog_in import AnalogIn
# import adafruit_ads1x15.ads1115 as ADS

# # Set up I2C and ADS1115
# i2c = busio.I2C(board.SCL, board.SDA)
# ads = ADS.ADS1115(i2c)
# chan = AnalogIn(ads, ADS.P0)

# R1 = 10000  # 10kΩ
# R2 = 2200   # 2.2kΩ

# def calibrate_zero():
#     total_readings = 400
#     zero_voltage = sum(chan.voltage for _ in range(total_readings)) / total_readings
#     return zero_voltage

# ZERO_VOLTAGE = calibrate_zero()

# def read_current():
#     voltage = chan.voltage
#     actual_voltage = voltage * (R1 + R2) / R2
#     print(f"Raw Voltage: {actual_voltage:.3f} V")
    
#     # Calculate current, adjusting for the zero voltage
#     current = (actual_voltage - ZERO_VOLTAGE) / 0.185
#     return current

# try:
#     while True:
#         current = read_current()
#         print(f"Current: {current:.3f} A")
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("Script stopped")


# WORKING CODE  

# import time
# import board
# import busio
# from adafruit_ads1x15.analog_in import AnalogIn
# import adafruit_ads1x15.ads1115 as ADS

# # Set up I2C and ADS1115
# i2c = busio.I2C(board.SCL, board.SDA)
# ads = ADS.ADS1115(i2c)
# chan = AnalogIn(ads, ADS.P0)

# R1 = 10000  # 10kΩ
# R2 = 2000   # 2.2kΩ

# def calibrate_zero():
#     total_readings = 100
#     zero_voltage = sum(chan.voltage for _ in range(total_readings)) / total_readings
#     print(f"Zero Voltage: {zero_voltage:.3f} V")  # Print for debugging
#     return zero_voltage

# ZERO_VOLTAGE = calibrate_zero()

# def read_current():
#     voltage = chan.voltage
#     actual_voltage = voltage * (R1 + R2) / R2
#     print(f"Raw Voltage: {actual_voltage:.3f} V")
    
#     # Calculate current with the zero voltage reference
#     current = (actual_voltage - ZERO_VOLTAGE) / 0.85
#     return current

# try:
#     while True:
#         current = read_current()
#         print(f"Current: {current:.3f} A")
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("Script stopped")


# sir faraz code 
# import time
# import board
# import busio
# from adafruit_ads1x15.analog_in import AnalogIn
# import adafruit_ads1x15.ads1115 as ADS
# from flask import Flask, render_template, jsonify

# app = Flask(__name__)

# # Set up I2C and ADS1115
# i2c = busio.I2C(board.SCL, board.SDA)
# ads = ADS.ADS1115(i2c)
# chan_current = AnalogIn(ads, ADS.P0)
# chan_voltage = AnalogIn(ads, ADS.P1)

# R1 = 10000  # 10kΩ
# R2 = 2200   # 2.2kΩ

# def calibrate_zero():
#     total_readings = 100
#     zero_voltage = sum(chan_current.voltage for _ in range(total_readings)) / total_readings
#     return zero_voltage

# ZERO_VOLTAGE = calibrate_zero()

# def read_current():
#     voltage = chan_current.voltage
#     actual_voltage = voltage * (R1 + R2) / R2
#     current = (actual_voltage - ZERO_VOLTAGE)
#     # current = (actual_voltage - ZERO_VOLTAGE) / 0.85  # Adjust as per your sensor's sensitivity
#     return current, actual_voltage

# @app.route('/')
# def index():
#     return render_template('index2.html')

# @app.route('/data')
# def data():
#     current, voltage = read_current()
#     return jsonify(current=current, voltage=voltage)

# if __name__ == '__main__':
#     app.run(debug=True)

#







# new
import time
import board
import busio
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Set up I2C and ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

# Create analog inputs
chan_current = AnalogIn(ads, ADS.P0)
chan_voltage = AnalogIn(ads, ADS.P1)

# Voltage divider resistances
R1 = 10000  # 10kΩ
R2 = 2200   # 2.2kΩ

def calibrate_zero():
    total_readings = 100
    zero_voltage = sum(chan_current.voltage for _ in range(total_readings)) / total_readings
    return zero_voltage

ZERO_VOLTAGE = calibrate_zero()


from voltage import read_voltage
from random import uniform
# def read_current_and_voltage():
#     # Read current voltage
#     voltage = chan_current.voltage
#     actual_voltage = voltage * (R1 + R2) / R2  # Calculate the actual voltage based on the divider

#     # Calculate current (adjust based on your sensor's sensitivity if needed)
#     current = (actual_voltage - ZERO_VOLTAGE)  # or / 0.85 if needed

#     return current, actual_voltage

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/data')
def data():
    # current, voltage = read_current_and_voltage()
    return jsonify(current=uniform(0,3.1), voltage=read_voltage)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
