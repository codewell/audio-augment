from setuptools import setup, find_packages


setup(
   name='audio_augment',
   version='0.0.4',
   description='Augmentation library for raw audio waveforms',
   author='Felix Abrahamsson',
   author_email='FelixAbrahamsson@github.com',
   keywords='audio sound augment augmentaiton deep machine learning pytorch',
   packages=['audio_augment'],
   install_requires=[
       'numpy',
       'librosa',
   ],
)
