class Entity():
    def __init__(self, key):
        # Initialize all components None
        self.key = key
        self.display = None
        self.kinematics = None
        self.gravity = None
        self.tilemap_collidable = None
        self.shape = None
        self.controller_input = None
        self.actions = None
        self.ai = None
        self.following = None
        self.orientation = None

        self.status = None

        self.running_floating_action = None
        self.jumping_action = None
        self.dashing_action = None
