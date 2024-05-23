import numpy as np

from simple_profiler import SimpleProfiler as sp


sp.instance().Load('output/profiler_22-05-2024-16:07:00.pkl')

num_samples = len(sp.instance()['Main'].recorded_times)

sp.instance().draw_timer_graph('Main', num_bins=5, normalise=False)
