import time
import psutil
import random

class Sender:
    def sendMessage(self,message):
        print(message)

class ActivityRecognizer:

    def __init__(self):
        self.refresh()

    def refresh(self):
        self.pids = psutil.pids()

    def getActivityType(self):
        self.refresh()
        pid = random.choice(self.pids)
        process = psutil.Process(pid)
        return process.name()

class PowerC:
    def __init__(self):
        self.state = "off"

    def getState(self):
        return self.state

    def on(self):
        self.state = "on"

    def off(self):
        self.state = "off"

class Application:
    def __init__(self):
        self.sender = Sender()
        self.activity_recognizer = ActivityRecognizer()
        self.power_c = PowerC()
        self.power_c.on()

    def run(self):
        while True:
            time.sleep(0.5)
            message = f"PC is {self.power_c.getState()}, application '{self.activity_recognizer.getActivityType()}' is running."
            self.sender.sendMessage(message)

a = Application()
a.run()