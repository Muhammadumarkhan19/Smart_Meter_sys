import time
import board
import jwt

import busio
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from RPLCD.i2c import CharLCD

# Firebase configuration
cred = credentials.Certificate('iot-thunder-firebase-adminsdk-l5sdf-09590f7f5e.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-thunder-default-rtdb.firebaseio.com/'
})







# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
ads.gain = 1
current_chan = AnalogIn(ads, ADS.P1)
voltage_chan = AnalogIn(ads, ADS.P2)

# Initialize the LCD using I2C
lcd = CharLCD('PCF8574', 0x27)  # Adjust the I2C address if necessary

REFERENCE_VOLTAGE = 5
SENSITIVITY = 1023.0

def read_current():
    raw_value = adc.read_adc(0, gain=GAIN)
    voltage = raw_value * (4.096 / 32767)  # Convert to voltage
    current = (voltage - 2.5) / 0.185  # For ACS712 5A
    return current



# def read_current():
    # voltage = current_chan.voltage
    # # current = (voltage - REFERENCE_VOLTAGE) / SENSITIVITY
    # return current

def read_voltage():
    voltage = voltage_chan.voltage
    return voltage

try:
    while True:
        current = read_current()
        voltage = read_voltage()
        
        # Print the readings
        print(f"Current: {current:.3f} A, Voltage: {voltage:.3f} V")
        
        # Prepare data
        data = {
            'current': current,
            'voltage': voltage,
            'timestamp': time.time()
        }

        # Send readings to Firebase
        try:
            db.reference('readings').push(data)
        except Exception as e:
            print(f"Failed to push data to Firebase: {e}")
        
        # Display on LCD
        lcd.clear()
        lcd.write_string(f"C: {current:.2f} A\nV: {voltage:.2f} V")

        time.sleep(1)

except KeyboardInterrupt:
    print("Script stopped")
