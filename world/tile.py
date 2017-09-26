class Tile():
    def __init__(self):
        pass

class EmptyTile(Tile):
    def __init__(self, special_properties = None):
        self.type = 'empty'
        self.special_properties = special_properties

class SolidTile(Tile):
    def __init__(self, special_properties = None):
        self.type = 'solid'

        self.special_properties = special_properties

class RampTile(Tile):
    def __init__(self, a, b, special_properties = None):
        self.type = 'ramp'
        self.a = a
        self.b = b

        self.special_properties = special_properties



class SlantTile(Tile):
    def __init__(self, special_properties = None):
        self.type = 'slant'
        self.a = a
        self.b = b

        self.special_properties = special_properties
