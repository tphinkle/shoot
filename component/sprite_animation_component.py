class SpriteAnimationComponent():
    def __init__(self):
        self.sprite_animations = []
        self.previous_sprite_type = None
        pass

class SpriteAnimation():
    def __init__(self):
        self.sprite_type = None
        self.conditions = []
        self.anticonditions = []
        self.sequence = []
        self.sprite_source_rects = []
        self.iter = 0
