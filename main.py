import numpy as np
from tqdm import tqdm

from simple_profiler import SimpleProfiler as sp

lens = [
    10000,
    50000,
    100000,
    500000,
    1000000,
    5000000,
    10000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
    50000000,
]

sp.instance().enable_checkpointing('checkpoints/', call_rate=10)

for i in tqdm(range(len(lens))):

    sp.instance()['Main'].start()
    data = np.random.randint(0, 100, size=(lens[i]))
    sp.instance()['Main'].stop()


sp.instance().generate_statistics()
sp.instance().save('output/')
