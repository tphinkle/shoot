class RunFloatActionComponent():
    def __init__(self):
        # State and modifiers
        self.name = 'runningfloating'
        self.status = 'inactive'
        self.mode = None
        self.timer = 0
        self.direction = None
        self.args = []
        self.period = 0



        self.running_base_speed = None
        self.floating_base_speed = None
        self.speed_augmentations = 0



    def running_speed(self):
        return self.running_base_speed + self.speed_augmentations

    def floating_speed(self):
        return self.floating_base_speed + self.speed_augmentations
