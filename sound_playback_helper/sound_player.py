from pydub import AudioSegment
from pydub.playback import play
from os import listdir
from os.path import isfile, join


class SoundPlayer(object):
    def __init__(self, path='Sounds/'):
        self.root_path = path
        self.current_index = 0
        self.loaded_sounds = self.load_all()

    def list_sounds(self):
        return [f for f in listdir(self.root_path) if isfile(join(self.root_path, f))]

    def load(self, name):
        fullName = self.root_path + name
        return AudioSegment.from_mp3(full_name)

    def load_all(self):
        return [AudioSegment.from_mp3(self.root_path + f) for f in listdir(self.root_path) if isfile(join(self.root_path, f))]

    def play(self, sound):
        play(sound)

    def play_rotated_sound(self):
        all_sounds = self.loaded_sounds
        if all_sounds == []:
            raise Exception('No sounds found in directory ' + self.root_path)
        if self.current_index >= len(all_sounds):
            self.current_index = 0
        sound = all_sounds[self.current_index]
        self.play(sound)
        self.current_index += 1
