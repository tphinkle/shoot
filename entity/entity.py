class Entity():
    def __init__(self, key):
        # Initialize all components None
        self.key = key
        self.display = None
        self.position = None
        self.velocity = None
        self.gravity = None
        self.acceleration = None
        self.tilemap_collidable = None
        self.shape = None
        self.controller_input = None
        self.actions = None
        self.ai = None
        self.following = None
        self.orientation = None
