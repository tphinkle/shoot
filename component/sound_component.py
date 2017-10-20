import sdl2.sdlmixer

class SoundComponent():
    def __init__(self):
        self.sound_queue = []





class Sound():
    def __init__(self, file_path):
        self.file_path = file_path
        self.playing = False
        pass


class LocalSound(Sound):
    sound_type = 'local'
    def __init__(self, file_path):
        Sound.__init__(self, file_path)

        self.source_x = None
        self.source_y = None


class AmbientSound(Sound):
    sound_type = 'ambient'

    def __init__(self, file_path):
        Sound.__init__(self, file_path)
