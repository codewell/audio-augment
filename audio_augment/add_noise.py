import numpy as np


def add_noise(audio, p=0.5, strength=0.007, p_gaussian=0.5):
    audio = audio.copy()
    if np.random.random() > p:
        return audio
    noise_amp = strength * np.random.uniform() * np.amax(audio)
    if np.random.random() < p_gaussian:
        audio += noise_amp * np.random.normal(size=len(audio))
    else:
        audio += noise_amp * np.random.uniform(size=len(audio))
    return audio
