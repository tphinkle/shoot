class KinematicsSystem():
    '''
    * Processes kinematics related to acceleration, velocity, proposed position
    '''

    def __init__(self):
        #self.acc_vel_exp = (.4/2.5)
        pass





    def UpdateKinematics(self, world, dt):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.kinematics != None:


                self.UpdateVelocity(entity, dt)
                self.UpdateProposedPosition(entity, dt)



    def UpdateVelocity(self, entity, dt):


        vx = entity.kinematics.vx
        vy = entity.kinematics.vy

        dvx_total = 0
        dvy_total = 0

        # x
        for key, source in entity.kinematics.sources.iteritems():

            if source.ax != 0:

                dvx = 0


                # Fix so this works for stoping
                print
                print

                # Target greater than current
                if source.target_vx >= vx:
                    dvx = source.ax*dt
                    if vx + dvx > source.target_vx:
                        dvx = source.target_vx - vx

                # Target smaller than current
                elif source.target_vx < vx:
                    print 'this should stop...'
                    print 'ax', source.ax

                    dvx = source.ax*dt
                    print 'vx', vx
                    print 'dvx', dvx
                    print 'target vx', source.target_vx
                    if vx + dvx < source.target_vx:
                        print 'a'
                        dvx = source.target_vx - vx
                        print 'new dvx', dvx




                dvx_total += dvx

                print dvx_total

            if source.ay != 0:

                dvy = 0

                # Positive source
                if source.target_vy >= 0:
                    dvy = source.ay*dt
                    if vy + dvy > source.target_vy:
                        dvy = source.target_vy - vy

                # Negative source
                elif source.target_vy < 0:
                    dvx = source.ay*dt
                    if vy + dvy < source.target_vy:
                        dvy = source.target_vy - vy


                dvy_total += dvy



        entity.kinematics.vx = vx + dvx_total

        print 'final velocity:', entity.kinematics.vx

        entity.kinematics.vy = vy + dvy_total


    def UpdateProposedPosition(self, entity, dt):


        entity.kinematics.x_proposed = entity.kinematics.x + entity.kinematics.vx*dt
        entity.kinematics.y_proposed = entity.kinematics.y + entity.kinematics.vy*dt



    def ValidatePosition(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.kinematics != None:
                entity.kinematics.x = entity.kinematics.x_proposed
                entity.kinematics.y = entity.kinematics.y_proposed
