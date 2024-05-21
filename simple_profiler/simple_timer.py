import time


class SimpleTimer:

    def __init__(self):
        self.total_time = 0
        self.start_time = None
        self.recorded_times = []

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None: raise Exception('Error, must call start before stoping the timer')
        t = time.time() - self.start_time
        self.total_time += t
        self.recorded_times.append(t)
        self.start_time = None
