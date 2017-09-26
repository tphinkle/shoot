class AccelerationSystem():

    '''
    * Updates velocity in x- and y-directions based on acceleration.
    '''



    for key, entity in world.entity_manager.entitys.iteritems():
        if entity.acceleration != None:
            entity.velocity.vx = entity.velocity.vx +\
             entity.acceleration.ax*dt
            entity.velocity.vy = entity.velocity.vy +\
             entity.acceleration.ay*dt**(self.acceleration_modifier)
