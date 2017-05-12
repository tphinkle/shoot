class Tile():
    def __init__(self):
        self.type = None

class EmptyTile(Tile):
    def __init__(self):
        self.type = 'empty'

class SolidTile(Tile):
    def __init__(self):
        self.type = 'solid'

class RampTile(Tile):
    def __init__(self, a, b):
        self.type = 'ramp'
        self.a = a
        self.b = b


class SlantTile(Tile):
    def __init__(self):
        self.type = 'slant'
        self.a = a
        self.b = b
