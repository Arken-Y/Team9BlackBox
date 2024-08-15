from subprocess import call

class call_device:
    
    def __init__(self, path):
        self.path = path
        
    def call_py(self):
        call(["python3", "{}".format(self.path)])

if __name__ == "__main__":
    """imu = call_device("/home/pi/Desktop/Senior_Design_Project/berryIMU.py")
    imu.call_py()
    
    gps = call_device("/home/pi/Desktop/Senior_Design_Project/GPS.py")
    gps.call_py()
    
    pressure = call_device("/home/pi/Desktop/Senior_Design_Project/Pressure_Sensor.py")
    pressure.call_py()"""
    
    execfile('berryIMU.py')
    execfile('Pressure_Sensor.py')