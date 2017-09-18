class MovementProcessSystem():
    def __init__(self):
        pass

    def ProcessMovement(self, world, dt):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.velocity != None:
                entity.position.x_proposed = entity.position.x + entity.velocity.vx*dt
                entity.position.y_proposed = entity.position.y + entity.velocity.vy*dt

    def ValidateMovement(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.velocity != None:
                entity.position.x = entity.position.x_proposed
                entity.position.y = entity.position.y_proposed
