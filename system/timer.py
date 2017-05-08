# Python standard library
import time

class Timer():
    def __init__(self, period):
        self.start_time = self.GetTime()
        self.period = period
        self.dt = 0

    def Update(self):
        t = self.GetTime()
        if t - self.start_time >= self.period:
            self.UpdateDt(t)
            self.RestartTimer(t)
            return True
        else:
            return False

    def UpdateDt(self, t):
        self.dt = t-self.start_time

    def RestartTimer(self, t):
        self.start_time = t

    def GetTime(self):
        return time.time()
