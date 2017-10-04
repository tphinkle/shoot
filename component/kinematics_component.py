

class KinematicsComponent():
    def __init__(self):


        # Position
        self.x = 0
        self.y = 0

        self.x_proposed = 0
        self.y_proposed = 0


        # Velocity
        self.vx_sources = {}
        self.vy_sources = {}

        self.vx = 0
        self.vy = 0

        # Acceleration
        self.ax_sources = {}
        self.ay_sources = {}
        self.ax = 0
        self.ay = 0


        # Damping
        self.dampingx = 0
        self.dampingy = 0

        # Source terms
        source_names = ['gravity', 'running_floating', 'jumping', 'dashing']
        self.sources = {name: KinematicsSource() for name in source_names}



class KinematicsSource():

    def __init__(self):
        # Target: accelerate up until a maximum point

        self.target_vx = None
        self.target_vy = None
        self.ax = 0
        self.ay = 0

        pass
