# Python standard library
import sys

# Game specific
import helper_systems


class MoveActionProcessingSystem(helper_systems.Subject):

    def __init__(self):

        helper_systems.Subject.__init__(self)

        pass


    '''
    PRE-TRIGGER
    '''

    def SetEntityTrigger(self, entity, command):
        if command['trigger'] == 'start':

            # start OK
            if CheckStartTriggerConditions(entity, command):
                entity.move_action.trigger_status = 'start'
                if command['direction'] == 'left':
                    entity.move_action.direction = 'left'
                elif command['direction'] == 'right':
                    entity.move_action.direction = 'right'

            # start not OK
            else:
                entity.move_action.trigger_status = 'none'

        elif command['trigger'] == 'stop':

            # stop OK
            if CheckStopTriggerConditions(entity, command):
                entity.move_action.trigger_status = 'stop'

            # stop not OK
            else:
                entity.move_action.trigger_status = 'none'

    def CheckStartTriggerConditions(self, entity, command):
        return (entity.move_action.active_status == 'inactive')


    def CheckStopTriggerConditions(self, entity, command):
        return (entity.move_action.active_status == 'active')


    '''
    Trigger
    '''

    def TriggerEntity(self, entity, action):
        if entity.move_action.trigger == 'start':
            self.TriggerEntityStart(entity)

        elif entity.move_action.trigger == 'start':
            self.TriggerEntityStop(entity)



    def TriggerEntityStart(self, entity):
        entity.move_action.trigger_status = 'none'

        entity.move_action.active_status = 'active'



    def TriggerEntityStop(self, entity):
        entity.move_action.trigger_status = 'none'

        entity.move_action.active_status = 'inactive'
