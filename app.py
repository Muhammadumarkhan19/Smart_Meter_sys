# from flask import Flask, render_template, redirect, url_for
# import RPi.GPIO as GPIO

# app = Flask(__name__)

# # Set up GPIO
# RELAY_PIN = 23  # Example GPIO pin for the relay
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(RELAY_PIN, GPIO.OUT)

# # Initialize the relay state
# relay_state = 0  # 0 for OFF, 1 for ON

# @app.route('/')
# def index():
#     return render_template('index.html', state=relay_state)

# @app.route('/toggle', methods=['POST'])
# def toggle():
#     global relay_state
#     relay_state = 1 - relay_state  # Toggle state: 0 -> 1 or 1 -> 0
#     GPIO.output(RELAY_PIN, relay_state)  # Set GPIO based on the new state
#     return redirect(url_for('index'))

# @app.route('/shutdown')
# def shutdown():
#     GPIO.cleanup()  # Clean up GPIO settings
#     return "GPIO cleaned up. Exiting..."

# if __name__ == '__main__':
#     try:
#         app.run(host='0.0.0.0', port=5000)
#     except KeyboardInterrupt:
#         GPIO.cleanup()  # Clean up GPIO settings on exit




import time
import board
import busio
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS
from flask import Flask, render_template, jsonify, redirect, url_for
import RPi.GPIO as GPIO

app = Flask(__name__)

# Set up I2C and ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan_current = AnalogIn(ads, ADS.P0)
chan_voltage = AnalogIn(ads, ADS.P1)

R1 = 10000  # 10kΩ
R2 = 2200   # 2.2kΩ

def calibrate_zero():
    total_readings = 100
    zero_voltage = sum(chan_current.voltage for _ in range(total_readings)) / total_readings
    return zero_voltage

ZERO_VOLTAGE = calibrate_zero()

def read_current():
    voltage = chan_current.voltage
    actual_voltage = voltage * (R1 + R2) / R2
    current = (actual_voltage - ZERO_VOLTAGE) / 0.85  # Adjust as per your sensor's sensitivity
    return current, actual_voltage

# Set up GPIO
RELAY_PIN = 23
  # Example GPIO pin for the relay
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)



# Initialize the relay state
relay_state = 0  # 0 for OFF, 1 for ON

@app.route('/')
def index():
    return render_template('index.html', state=relay_state)

@app.route('/data')
def data():
    current, voltage = read_current()
    return jsonify(current=current, voltage=voltage)

@app.route('/toggle', methods=['POST'])
def toggle():
    global relay_state
    relay_state = 1 - relay_state  # Toggle state: 0 -> 1 or 1 -> 0
    GPIO.output(RELAY_PIN, relay_state)  # Set GPIO based on the new state
    return redirect(url_for('index'))

@app.route('/shutdown')
def shutdown():
    GPIO.cleanup()  # Clean up GPIO settings
    return "GPIO cleaned up. Exiting..."

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()  # Clean up GPIO settings on exit
