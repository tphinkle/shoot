# Game specific
import helper_systems

class SoundSystem(helper_systems.Observer):

    def __init__(self):
        helper_systems.Observer.__init__(self)

        self.event_processing = {}


        # Sound effects
        self.event_processing


        self.event_processing['busterinactive'] = self.BusterInactive
        self.event_processing['chargebusterinactive'] = self.ChargeBusterInactive


    def Update(self, world):
        for key, entity in world.entity_manager.entities.iteritems():
            if entity.sound:
                pass

    pass




    def OnNotify(self, entity, event):
        if event in self.event_processing.keys():
            self.event_processing[event](entity)
        else:
            pass
    def ChargeBusterInactive(self, entity):
        pass

    def BusterInactive(self, entity):
        pass
