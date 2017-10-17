# Python standard library


class StatusProcessingSystem():


    def __init__(self):


        pass

    def ProcessStatus(self, world):
        for key, entity in world.entity_manager.entities.iteritems():
            if entity.status != None:

                self.ProcessHP(entity)
                self.ProcessStatusEffects(entity)

    def ProcessHP(self, entity):

        if entity.status.dead == False:
            if entity.status.hp == 0:
                entity.status.hp = -1
                entity.status.dead = True


    def ProcessStatusEffects(self, entity):
        # Time-based statuses
        if entity.status.frozen:
            self.ApplyFrozenEffect(entity)

        else:
            self.RemoveFrozenEffect(entity)



    def ApplyFrozenEffect(self, entity):
        entity.kinematics.dampingx = 100
        entity.status.frozen = False

    def RemoveFrozenEffect(self, entity):
        entity.kinematics.dampingx = 0
