#! /bin/sh
echo "Start?"
read x
if [ ${x} = "y" ]
then
	python GPS.py & python berryIMU.py
	LASTPID=$!
	read y
	if [ ${y} = "q" ]
	then
		killall $LASTPID
	fi  
fi
shutdown --reboot -f
