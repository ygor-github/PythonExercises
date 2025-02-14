import time
import os
class Cronometro:
    def __init__(self, seconds = 0,  minutes = 0, hours = 0):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def __repr__(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def increase(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes >= 60:
            self.minutes = 0
            self.hours += 1

    def start(self):
        while True:
            os.system('clear')
            print(self)
            self.increase()
            time.sleep(1)

cronometro1 = Cronometro()

cronometro1.start()