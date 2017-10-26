# Python standard library
import sys

# Game-specific
import active_component


class ShootActionComponent(active_component.Action):


    def __init__(self):
        active_component.Action.__init__(self, 'shoot', 'shoot')

        self.guns = {}

    def AttachGun(self, gun):
        self.guns[gun.name] = gun

class GunChargeActionComponent(active_component.Action):
    def __init__(self):
        pass


class Gun(object):
    def __init__(self):
        self.name = None
        self.owner = None
        self.max_bullets_out = 0
        self.bullets_out = 0
        self.cooldown = 0
        self.cooldown_timer = 0
        self.bullet_name = None
        self.status = 'inactive'

        self.x_offset = 0
        self.y_offset = 0




class NormalGun(Gun):
    type = 'normal'
    def __init__(self):
        Gun.__init__(self)


class ChargeGun(Gun):
    type = 'charge'
    def __init__(self):
        Gun.__init__(self)

        self.charge_timer = 0
        self.charge_times = []
        self.bullet_types = []
