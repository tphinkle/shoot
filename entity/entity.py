class Entity():
    def __init__(self, type):
        # Initialize all components None
        self.type = type
        self.id = None
        self.key = None





        self.display = None
        self.sprite_animation = None
        self.kinematics = None
        self.gravity = None
        self.friction = None
        self.tilemap_collidable = None
        self.shape = None
        self.controller_input = None
        self.actions = None
        self.ai = None
        self.following = None
        self.orientation = None
        self.factory = None

        self.status = None

        self.running_floating_action = None
        self.jumping_action = None
        self.dashing_action = None
        self.panning_action = None
        self.shooting_action = None

        self.on_death = None
