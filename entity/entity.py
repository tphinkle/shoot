class Entity():
    def __init__(self, type):
        # Initialize all components None
        self.type = type
        self.id = None
        self.key = None




        self.sound = None
        self.display = None
        self.sprite_animation = None
        self.kinematics = None
        self.gravity = None
        self.friction = None
        self.tilemap_collidable = None
        self.shape = None
        self.controller_input = None


        self.active = None
        '''
        self.move_action = None
        self.dash_action = None
        self.shoot_action = None
        self.jump_action = None
        '''

        self.ai = None
        self.following = None
        self.orientation = None
        self.factory = None

        self.status = None


        self.on_death = None
