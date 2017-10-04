class DashingActionComponent():
    def __init__(self):
        # State and modifiers
        self.name = 'dashing'
        self.base_speed = None
        self.speed_augmentations = 0
        self.status = 'inactive'
        self.args = []
        self.period = 1.

        self.duration = 1.
        self.timer = 0.

        self.direction = None


    def speed(self):
        return self.base_speed + self.speed_augmentations
