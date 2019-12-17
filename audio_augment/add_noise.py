import numpy as np


def add_noise(audio, p=0.5, p_gaussian=0.5, high=0.01, low=0.01):
    audio = audio.copy()
    if np.random.random() > p:
        return audio
    strength = np.random.random() * (high - low) + low
    noise_amp = strength * np.random.uniform() * np.amax(audio)
    if np.random.random() < p_gaussian:
        audio += noise_amp * np.random.normal(size=len(audio))
    else:
        audio += noise_amp * np.random.uniform(size=len(audio))
    return audio
