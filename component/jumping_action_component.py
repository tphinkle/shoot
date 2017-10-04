class JumpingActionComponent():
    def __init__(self):
        # State and modifiers
        self.name = 'jumping'
        self.status = 'inactive'
        self.timer = 0
        self.args = []
        self.period = 0

        self.initial_acceleration = 0
        self.increment_acceleration = 0

        self.speed_augmentations = 0
        self.base_speed = 0
        self.double_jump_available = False




    def speed(self):
        return self.base_speed + self.speed_augmentations
