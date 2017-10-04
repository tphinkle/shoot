class PanningActionComponent():
    def __init__(self):
        # State and modifiers
        self.status = 'inactive'
        self.args = []
        self.period = 0
        self.timer = 0
        self.xdirection = None
        self.ydirection = None


        # Constants
        self.xspeed = 0
        self.yspeed = 0
