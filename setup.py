from setuptools import setup

setup(
    name='Sound Playback Helper',
    url='https://github.com/kburgon/sound-playback-helper',
    author='Kevin Burgon',
    author_email='kein.burgon@gmail.com',
    packages=['sound_playback_helper'],
    install_requires=['pydub'],
    version='0.1',
    license='MIT',
    description='A helper module, providing basic playback options for local files.',
    long_description=open('README.md').read()
)
