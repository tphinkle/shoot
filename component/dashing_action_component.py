class DashingActionComponent():
    def __init__(self):
        self.base_speed = None
        self.speed_augmentations = 0
        self.status = 'inactive'

        self.duration = 1.
        self.timer = 0.

        self.direction = None


    def speed(self):
        return self.base_speed + self.speed_augmentations
