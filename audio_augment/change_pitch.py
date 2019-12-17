import numpy as np
import librosa


def change_pitch(audio, sampling_rate, p=0.5, pitch_pm=4, bins_per_octave=24):
    audio = audio.copy()
    if np.random.random() > p:
        return audio
    pitch_change = pitch_pm * (np.random.uniform() - 0.5) * 2
    return librosa.effects.pitch_shift(
        audio,
        sampling_rate,
        n_steps=pitch_change,
        bins_per_octave=bins_per_octave
    )
