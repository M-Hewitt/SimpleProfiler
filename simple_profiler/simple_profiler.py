import pickle
from datetime import datetime

import numpy as np
from matplotlib import pyplot as plt

from simple_profiler.simple_timer import SimpleTimer


class SimpleProfiler:
    """
    Got this singleton pattern from:
    https://python-patterns.guide/gang-of-four/singleton/
    """

    _instance = None
    timers = {}

    num_calls = 0
    checkpoint_location = None
    call_rate = None

    recording_rate = None

    def __init__(self):
        raise Exception('Singleton, call instance instead.')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            # Put any initialization here.

        cls._instance.num_calls += 1

        if cls._instance.call_rate:
            cls._instance.checkpoint()

        return cls._instance

    def set_recording_rate(self, recording_rate):
        self.recording_rate = recording_rate

    def __getitem__(self, item):
        if item not in self.timers:
            self.timers[item] = SimpleTimer(self.recording_rate)

        return self.timers[item]

    def generate_statistics(self):
        for i, timer in self.timers.items():
            timer.close_timer()
            print('Timer {}: {} seconds'.format(i, timer.total_time))

    def save(self, output_path):
        with open('{}/profiler_{}.pkl'.format(output_path, datetime.now().strftime("%d-%m-%Y-%H:%M:%S")), 'wb') as f:
            pickle.dump(self.timers, f, protocol=pickle.HIGHEST_PROTOCOL)

    def enable_checkpointing(self, checkpoint_path, call_rate=100):
        self.checkpoint_location = checkpoint_path
        self.call_rate = call_rate

    def checkpoint(self):
        if self.num_calls % self.call_rate == 0:
            self.save(self.checkpoint_location)

    @staticmethod
    def Load(path):

        with open(path, 'rb') as f:
            data = pickle.load(f)
            SimpleProfiler.instance().timers = data

    def draw_timer_graph(self, t, num_bins=None, normalise=True):
        timer = self.timers[t]
        print('Timer {}: {} seconds'.format(t, timer.total_time))

        if num_bins is None:
            bins = timer.recorded_times
            x_axis = np.arange(len(bins))
        else:
            bin_widths = len(timer.recorded_times)//num_bins

            bins = np.array([np.mean(timer.recorded_times[i*bin_widths:(i+1)*bin_widths]) for i in range(num_bins)])

            x_axis = np.arange(num_bins)

        if normalise:
            bins = bins/np.sum(bins)

        plt.figure()
        plt.title(t)
        plt.bar(x_axis, bins)
        plt.show()
