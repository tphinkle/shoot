class ShootingActionComponent(object):
    def __init__(self):
        self.guns = {}


class Gun(object):
    def __init__(self):
        self.owner = None
        self.bullets_out = 0
        self.cooldown = 0
        self.cooldown_timer = 0
        self.bullet_type = None
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
