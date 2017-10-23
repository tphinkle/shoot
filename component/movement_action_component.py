class MovementActionComponentSystem():
    def __init__(self):
        pass


class NormalMovementActionComponent(MovementActionComponentSystem):
    def __init__(self):
        MovementActionComponentSystem.__init__(self)

        # State and modifiers
        self.movement_type = 'normal'
        self.status = 'inactive'
        self.mode = None
        self.timer = 0
        self.direction = None
        self.args = []
        self.period = 0



        self.running_base_speed = None
        self.floating_base_speed = None


class FreeMovementActionComponent(MovementActionComponentSystem):
    def __init__(self):
        MovementActionComponentSystem.__init__(self)

        # State and modifiers
        self.movement_type = 'free'
        self.status = 'inactive'
        self.mode = None
        self.timer = 0
        self.direction = None
        self.args = []
        self.period = 0

        #self.allowed_active_states.append()



        self.speed = None
