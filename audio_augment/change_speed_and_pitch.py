import numpy as np


def change_speed_and_pitch(audio, p=0.5, low=0.85, high=1.15):
    audio = audio.copy()
    if np.random.random() > p:
        return audio
    length_change = np.random.uniform(low=low, high=high)
    speed_fac = 1.0  / length_change
    interpolated = np.interp(
        np.arange(0, len(audio), speed_fac),
        np.arange(0, len(audio)),
        audio
    )
    min_len = min(len(audio), len(interpolated))
    audio *= 0
    audio[0 : min_len] = interpolated[0 : min_len]
    return audio
