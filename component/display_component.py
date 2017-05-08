import sdl2

class DisplayComponent():
    def __init__(self, filepath):
        self.filepath = filepath
        self.texture = None
        self.source_rect = None
        self.z = 0
