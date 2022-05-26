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
    listen(prox_sensors)

    while True:
        # print_id_value(prox_sensors)
        id_0 = oProx_0.get_id()
        id_3 = oProx_7.get_id()
        
        val_0 = oProx_0.get_proximity()
        val_3 = oProx_3.get_proximity()
        print(id_0, val_0)
        print(id_3, val_3)
        time.sleep(.1)
    
def listen(prox_sensors):
    for sensor in prox_sensors:
        sensor.begin()

def print_id_value(prox_sensors):
    for sensor in prox_sensors:
        prox_value = sensor.get_proximity()
        prox_id = sensor.get_id()
        print(prox_id, prox_value)
        
def set_channels():
    mux = qwiic.QwiicTCA9548A()
    mux.list_channels()
    mux.enable_channels([0,3,4,7])
    # mux.enable_channels(0)
    # mux.enable_channels(3)
    # mux.enable_channels(4)
    # mux.enable_channels(7)
    
def main():
    # set_channels()
    runExample()
    
main()