class RunningFloatingActionComponent():
    def __init__(self):
        self.running_base_speed = None
        self.floating_base_speed = None
        self.speed_augmentations = 0
        self.active = False
        self.direction = None


    def running_speed(self):
        return self.running_base_speed + self.speed_augmentations

    def floating_speed(self):
        return self.floating_base_speed + self.speed_augmentations
