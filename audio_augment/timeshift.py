import numpy as np


def timeshift(audio, p=0.5, strength=0.2):
    audio = audio.copy()
    if np.random.random() > p:
        return audio
    timeshift_factor = strength * (np.random.uniform() - 0.5) * 2
    start = int(len(audio) * timeshift_factor)
    padding = (start, 0) if (start > 0) else (0, -start)
    return np.pad(audio, padding, mode='constant')[0 : len(audio)]
