# Python standard library
import sys

# Game-specific
import active_component


class DashActionComponent(active_component.Action):
    def __init__(self):
        active_component.Action.__init__(self, action_class = 'dash', action_name = 'dash')


        self.base_speed = None
        self.speed_augmentations = 0

        self.args = []
        self.period = 1.

        self.duration = 1.
        self.timer = 0.

        self.direction = None


    def speed(self):
        return self.base_speed + self.speed_augmentations
