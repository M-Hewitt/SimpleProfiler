import numpy as np

from simple_profiler import SimpleProfiler as sp


sp.instance().Load('checkpoints/profiler_21-05-2024-21:07:53.pkl')

num_samples = len(sp.instance()['Main'].recorded_times)

sp.instance().draw_timer_graph('Main', num_bins=10, normalise=False)
