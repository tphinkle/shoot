class KinematicsSystem():
    '''
    * Processes kinematics related to acceleration, velocity, proposed position
    '''

    def __init__(self):
        self.acc_vel_exp = (.4/2.5)
        pass


    def ProcessAcceleration(self, world, dt):
        for key, entity in world.entity_manager.entitys.iteritems():


            if entity.kinematics != None:
                # Acceleration
                entity.kinematics.vx += entity.kinematics.ax*dt
                entity.kinematics.vy += entity.kinematics.ay*dt**self.acc_vel_exp

                # Damping
                if entity.kinematics.vx < 0:
                    entity.kinematics.vx += entity.kinematics.dampingx*dt**self.acc_vel_exp

                if entity.kinematics.vx > 0:
                    entity.kinematics.vx -= entity.kinematics.dampingx*dt**self.acc_vel_exp


    def ProcessMovement(self, world, dt):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.kinematics != None:
                entity.kinematics.x_proposed = entity.kinematics.x + entity.kinematics.vx*dt
                entity.kinematics.y_proposed = entity.kinematics.y + entity.kinematics.vy*dt


    def ValidateMovement(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.kinematics != None:
                entity.kinematics.x = entity.kinematics.x_proposed
                entity.kinematics.y = entity.kinematics.y_proposed
