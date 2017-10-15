# Python standard library


class StatusProcessingSystem():


    def __init__(self):


        pass


    def ProcessStatusEffects(self, world):
        for key, entity in world.entity_manager.entities.iteritems():
            if entity.status != None:


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
