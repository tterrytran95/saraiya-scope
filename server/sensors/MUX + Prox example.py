import time
import board
import qwiic_tca9548a
import qwiic_proximity
import adafruit_tca9548a
import sys
import adafruit_vcnl4040

# Create I2C bus as normal
i2c = board.I2C()

# Create the TCA9548A object and give it the I2C bus
#tca = qwiic_tca9548a.QwiicTCA9548A()
tca = adafruit_tca9548a.TCA9548A(i2c)

prox1 = adafruit_vcnl4040.VCNL4040(tca[0])
prox2 = adafruit_vcnl4040.VCNL4040(tca[3])
prox3 = adafruit_vcnl4040.VCNL4040(tca[4])
prox4 = adafruit_vcnl4040.VCNL4040(tca[7])

while True:
    p1 = prox1.proximity
    p2 = prox2.proximity
    p3 = prox3.proximity
    p4 = prox4.proximity
    
    print('prox1:', p1)
    print('prox2:', p2)
    print('prox3:', p3)
    print('prox4:', p4)
    time.sleep(3)