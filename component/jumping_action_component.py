class JumpingActionComponent():
    def __init__(self):
        self.active = False

        self.speed_augmentations = 0
        self.base_speed = 0



    def speed(self):
        return self.base_speed + self.speed_augmentations
