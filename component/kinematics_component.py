

class KinematicsComponent():
    def __init__(self):


        # Position
        self.x = 0
        self.y = 0

        self.x_proposed = 0
        self.y_proposed = 0


        # Velocity
        self.vx = 0
        self.vy = 0

        # Acceleration
        self.ax = 0
        self.ay = 0
        self.x_sources = []
        self.y_sources = []



class KinematicsXSource():

    def __init__(self, ax = 0, target_vx = 0):
        self.ax = ax
        self.target_vx = target_vx


        pass

class KinematicsYSource():

    def __init__(self, ay = 0, target_vy = 0):
        self.ay = ay
        self.target_vy = target_vy


        pass
