from pydub import AudioSegment
from pydub.playback import play
from os import listdir
from os.path import isfile, join


class SoundPlayer(object):
    def __init__(self, path='Sounds/'):
        self.root_path = path
        self.current_index = 0

    def list_sounds(self):
        return [f for f in listdir(self.root_path) if isfile(join(self.root_path, f))]

    def play(self, sound_name):
        print('playing name ' + sound_name)
        full_name = self.root_path + sound_name
        song = AudioSegment.from_mp3(full_name)
        play(song)

    def play_rotated_sound(self):
        all_sounds = self.list_sounds()
        if all_sounds == []:
            raise Exception('No sounds found in directory ' + self.root_path)
        if self.current_index == len(all_sounds):
            self.current_index = 0
        sound = all_sounds[self.current_index]
        self.current_index = 0
        self.play(sound)
        self.current_index += 1
