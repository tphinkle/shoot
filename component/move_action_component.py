# Python standard library
import sys

# Game-specific
import active_component


class NormalMoveActionComponent(active_component.Action):
    def __init__(self):


        active_component.Action.__init__(self, 'move', 'normalmove')

        # State and modifiers
        self.movement_type = 'normal'
        self.mode = None
        self.timer = 0
        self.direction = None
        self.args = []
        self.period = 0



        self.running_base_speed = None
        self.floating_base_speed = None


class FreeMoveActionComponent(active_component.Action):
    def __init__(self):
        active_component.Action.__init__(self, 'move', 'freemove')

        # State and modifiers
        self.movement_type = 'free'

        self.mode = None
        self.timer = 0
        self.direction = None
        self.args = []
        self.period = 0

        #self.allowed_active_states.append()



        self.speed = None
