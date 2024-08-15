from guizero import App, Text, PushButton
import subprocess


#time.sleep(15)
def run_program():
    process1 = subprocess.Popen(["sh", "/home/pi/Desktop/Senior_Design_Project/start.sh"])
    welcome_message.value = "Program Running"

def stop_program():
    process2 = subprocess.Popen(["sh", "/home/pi/Desktop/Senior_Design_Project/stop.sh"])
    welcome_message.value = "Program Stop"

app = App(title="Aerobatic BlackBox")
welcome_message = Text(app, text="Welcome on Board!")
start = PushButton(app, command=run_program, text="Run Program")
stop = PushButton(app, command=stop_program, text="Stop Program")

app.display()
