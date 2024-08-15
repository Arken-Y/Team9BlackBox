import subprocess
#subprocess.call("./main")
#subprocess.call("python3", "Pressure_Sensor.py")
subprocess.call("python", "GPS.py")

Output_data = IMU_data = Pressure_data = GPS_data = ""

with open(IMU_data.txt) as fp:
    IMU_data = fp.read()

with open(Pressure_data.txt) as fp:
    Pressure_data = fp.read()
    
with open(GPS_data.txt) as fp:
    GPS_data = fp.read()
    
Output_data = IMU_data + "\n" + Pressure_data + "\n" + GPS_data

print(Output_data)
file1 = open (output.fdr, "a")
file1.write(Output_data)
file1.close()
