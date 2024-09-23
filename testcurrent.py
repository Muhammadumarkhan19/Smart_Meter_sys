import time
import board
import busio
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS

# Set up I2C and ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)  # Change P0 to your selected channel

# User-defined sensitivity and reference voltage for the sensor
SENSITIVITY = 0.185  # Adjust based on your ACS712 model

# Function to calibrate zero voltage
def calibrate_zero(total_readings=100):
    zero_voltage = sum(chan.voltage for _ in range(total_readings)) / total_readings
    print(f"Calibrated Zero Voltage: {zero_voltage:.3f} V")
    return zero_voltage

# Calibrate and get the zero voltage
ZERO_VOLTAGE = calibrate_zero()

def read_current():
    voltage = chan.voltage  # Read voltage from ADC
    current = (voltage - ZERO_VOLTAGE) / SENSITIVITY
    return current

try:
    while True:
        current = read_current()
        print(f"Current: {current:.3f} A")
        time.sleep(1)
except KeyboardInterrupt:
    print("Script stopped")

