class SpriteAnimationComponent():
    def __init__(self):
        self.animations = []
        self.active_animation = None


class Animation():
    def __init__(self, name):
        self.name = name
        self.counter = 0
        self.total_frames = 0
        self.rects = []
        self.type = None
