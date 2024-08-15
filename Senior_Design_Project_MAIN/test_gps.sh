#! /bin/sh

python3 Pressure_Sensor.py &
LASTPID=$!
read x
if [ ${x} = "y" ]
then
	kill $LASTPID
fi
