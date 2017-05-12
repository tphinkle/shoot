class AccelerationSystem():
    def   __init__(self):
        pass
    def ProcessAcceleration(self, world, dt):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.acceleration != None:
                entity.velocity.vx = entity.velocity.vx + entity.acceleration.ax*dt
                entity.velocity.vy = entity.velocity.vy + entity.acceleration.ay*dt**(.8/2.5)
