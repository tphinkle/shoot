class EntityCleanupSystem():

    def __init__(self):
        pass

    def CleanupEntities(self, world):
        for key, entity in world.entity_manager.entities.iteritems():
            if entity.status != None:
                if entity.status.hp == -1:
                    entity_manager.new_dead_entities.append(entity)
