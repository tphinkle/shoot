class KinematicsSystem():
    '''
    * Processes kinematics related to acceleration, velocity, proposed position
    '''

    def __init__(self):
        #self.acc_vel_exp = (.4/2.5)
        pass





    def UpdateKinematics(self, world, dt):
        for key, entity in world.entity_manager.entities.iteritems():
            if entity.kinematics != None:

                self.UpdateVelocity(entity, dt)
                self.UpdateProposedPosition(entity, dt)



    def UpdateVelocity(self, entity, dt):


        vx = entity.kinematics.vx

        dvx_total = 0

        x_sources = self.SortXSources(entity.kinematics.x_sources)



        for x_source in x_sources:

            dvx = 0

            # Target greater than current
            if x_source.target_vx > vx:
                dvx = x_source.ax*dt
                if vx + dvx > x_source.target_vx:
                    dvx = x_source.target_vx - vx

            # Target smaller than current

            elif x_source.target_vx < vx:

                dvx = x_source.ax*dt

                if vx + dvx < x_source.target_vx:

                    dvx = x_source.target_vx - vx



            vx += dvx
            #dvx_total += dvx



        #entity.kinematics.vx = vx + dvx_total
        entity.kinematics.vx = vx
        entity.kinematics.x_sources = []

        vy = entity.kinematics.vy

        dvy_total = 0
        y_sources = self.SortYSources(entity.kinematics.y_sources)


        for y_source in y_sources:

            dvy = 0

            # Target greater than current
            if y_source.target_vy >= vy:
                dvy = y_source.ay*dt
                if vy + dvy > y_source.target_vy:
                    dvy = y_source.target_vy - vy

            # Target smaller than current
            elif y_source.target_vy < vy:
                dvy = y_source.ay*dt

                if vy + dvy < y_source.target_vy:

                    dvy = y_source.target_vy - vy


            dvy_total += dvy



        entity.kinematics.vy = vy + dvy_total


        entity.kinematics.y_sources = []


    def SortXSources(self, x_sources):
        x_sources.sort(key = lambda x_source: abs(x_source.target_vx))
        return x_sources


    def SortYSources(self, y_sources):
        y_sources.sort(key = lambda y_source: abs(y_source.target_vy))
        return y_sources


    def UpdateProposedPosition(self, entity, dt):


        entity.kinematics.x_proposed = entity.kinematics.x + entity.kinematics.vx*dt
        entity.kinematics.y_proposed = entity.kinematics.y + entity.kinematics.vy*dt




    def ValidatePosition(self, world):
        for key, entity in world.entity_manager.entities.iteritems():
            if entity.kinematics != None:
                entity.kinematics.x = entity.kinematics.x_proposed
                entity.kinematics.y = entity.kinematics.y_proposed
