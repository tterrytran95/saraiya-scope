import qwiic_i2c                    # I2C bus driver package
import qwiic_proximity
import qwiic
import time
import sys

def runExample():

    print("\nSparkFun Proximity Sensor VCN4040 Example 1\n")
    
    oProx_0 = qwiic_proximity.QwiicProximity()
    oProx_3 = qwiic_proximity.QwiicProximity()
    oProx_4 = qwiic_proximity.QwiicProximity()
    oProx_7 = qwiic_proximity.QwiicProximity()

    #if oProx.isConnected() == False:
    set_channels()
    
    if (oProx_0.connected == False or oProx_3.connected == False or oProx_4.connected == False or oProx_7.connected == False):
        print("The Qwiic Proximity device isn't connected to the system. Please check your connection", file=sys.stderr)
        return
    prox_sensors = [oProx_0, oProx_3, oProx_4, oProx_7]
    print(oProx_0.get_id())
    print(oProx_3.get_id())
    print(oProx_4.get_id())
    print(oProx_7.get_id())
    listen(prox_sensors)

    while True:
        print_id_value(prox_sensors)
        time.sleep(.1)
    
def listen(prox_sensors):
    for sensor in prox_sensors:
        out = sensor.begin()

def print_id_value(prox_sensors):
    for sensor in prox_sensors:
        prox_value = sensor.get_proximity()
        # prox_id = sensor.get_id()
        prox_id = property(get_id)
        print(prox_id, prox_value)
        
def set_channels():
    mux = qwiic.QwiicTCA9548A() # create the multiplexer 
    print(mux.list_channels())
    chans = mux.enable_channels([0,3,4,7])
    print(chans)
    # mux.enable_channels(0)
    # mux.enable_channels(3)
    # mux.enable_channels(4)
    # mux.enable_channels(7)
    
def main():
    # set_channels()
    runExample()
    
main()