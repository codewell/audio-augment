import numpy as np
import librosa


def change_speed(audio, p=0.5, low=0.8, high=1.2):
    if np.random.random() > p:
        return audio
    speed_change = np.random.uniform(low=low, high=high)
    stretched = librosa.effects.time_stretch(audio, speed_change)
    min_len = min(len(audio), len(stretched))
    audio *= 0
    audio[0 : min_len] = stretched[0 : min_len]
    return audio
