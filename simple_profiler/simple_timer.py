import time

import numpy as np


class SimpleTimer:

    def __init__(self, amount_of_data=None):
        self.total_time = 0
        self.amount_of_data = amount_of_data
        self.start_time = None
        self.recorded_times = []
        self.current_times = []

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None: raise Exception('Error, must call start before stoping the timer')
        t = time.time() - self.start_time
        self.total_time += t
        if self.start_time:
            self.current_times.append(t)
            if len(self.current_times) == self.amount_of_data:
                self.recorded_times.append(np.mean(self.current_times))
                self.current_times = []
        else:
            self.recorded_times.append(t)
        self.start_time = None

    def close_timer(self):
        if len(self.current_times) > 0:
            self.recorded_times.append(np.mean(self.current_times))
            self.current_times = []
