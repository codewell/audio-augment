import numpy as np


def change_dynamic_range(audio, p=0.5, low=0.4, high=1.2):
    if np.random.random() > p:
        return audio
    return audio * np.random.uniform(low=low, high=high)
