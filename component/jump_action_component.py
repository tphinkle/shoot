# Python standard library
import sys

# Game-specific
import active_component

class JumpActionComponent(active_component.Action):
    def __init__(self):
        active_component.Action.__init__(self, action_class = 'jump', action_name = 'jump')


        self.timer = 0
        self.args = []
        self.period = 0

        self.initial_acceleration = 0
        self.increment_acceleration = 0

        self.base_speed = 0


class AirJumpActionComponent(active_component.Action):
    def __init__(self):
        active_component.Action.__init__(self, action_class = 'jump', action_name = 'airjump')


        # State and modifiers

        self.timer = 0
        self.args = []
        self.period = 0

        self.initial_acceleration = 0
        self.increment_acceleration = 0

        self.base_speed = 0
