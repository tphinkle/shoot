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

        self.base_speed = 0


class AirJumpingActionComponent():
    def __init__(self):
        # State and modifiers
        self.name = 'airjump'
        self.status = 'inactive'
        self.timer = 0
        self.args = []
        self.period = 0

        self.initial_acceleration = 0
        self.increment_acceleration = 0

        self.base_speed = 0
