# /etc/init.d/test_code.py
### BEGIN INIT INFO
# Provides:          test_code.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

from tkinter import * 
import tkinter.messagebox
import time

time.sleep(5)
root=Tk() 
result=tkinter.messagebox.askquestion('Installation','Do you want to install this anyway?')
if result=='yes':
    theLabel=Label(root,text="Enjoy this software.") #To insert a text
    theLabel.pack()
else:
    root.destroy() #Closing Tkinter window forcefully.
root.mainloop()