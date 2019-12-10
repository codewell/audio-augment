# Audio Augment
Augmentation library for raw audio waveforms.

## Installation
`pip install git+https://github.com/codewell/audio-augment.git`

## Example
### PyTorch
```
from torchvision import transforms
from functools import partial
import audio_augment


def get_audio_augmenter(sampling_rate):
    return transforms.Compose([
        partial(audio_augment.change_speed_and_pitch, p=0.5),
        partial(audio_augment.change_pitch, p=0.5, sampling_rate=sampling_rate),
        partial(audio_augment.change_speed, p=0.5),
        partial(audio_augment.change_dynamic_range, p=0.5),
        partial(audio_augment.add_noise, p=0.5),
        partial(audio_augment.timeshift, p=0.5),
    ])


random_noise_audio = np.random.randn(10000)
augmentor = get_audio_augmenter(sampling_rate=16000)
augmented_audio = augmentor(random_noise_audio)
```

## Benchmarks
8 second clip, sampling rate 16000

| Function               | Time [s]          |
| ---------------------- |-------------------|
| change_speed_and_pitch | 1.54 ms ± 22.7 µs |
| change_pitch           | 109 ms ± 1.88 ms  |
| change_speed           | 33.7 ms ± 2.52 ms |
| change_dynamic_range   | 105 µs ± 916 ns   |
| add_noise              | 2.37 ms ± 105 µs  |
| timeshift              | 41 µs ± 1.06 µs   |
