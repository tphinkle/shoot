# Python standard library
import sys


# Game specific
sys.path.append('../component/')
import kinematics_component

sys.path.append('../functions/')
import constants

import helper_systems



class DashActionProcessingSystem(helper_systems.Subject):

    def __init__(self):

        # Initialize observer class
        helper_systems.Subject.__init__(self)

    '''
    PRE-TRIGGER
    '''

    def SetEntityTrigger(self, entity, command):
        if command['trigger'] == 'start':

            # start OK
            if CheckStartTriggerConditions(entity, command):
                entity.dash_action.trigger_status = 'start'
                entity.dash_action.direction = entity.orientation.xorientation

            # start not OK
            else:
                entity.dash_action.trigger_status = 'none'

        elif command['trigger'] == 'stop':

            # stop OK
            if CheckStopTriggerConditions(entity, command):
                entity.dash_action.trigger_status = 'stop'

            # stop not OK
            else:
                entity.dash_action.trigger_status = 'none'

    def CheckStartTriggerConditions(self, entity, command):

        return ((entity.dash_action.active_status == 'inactive')
            and (entity.dash_action.cooldown_timer > entity.dash_action.cooldown)
            and (entity.gravity.grounded == True))


    def CheckStopTriggerConditions(self, entity, command):
        return (entity.dash_action.active_status == 'active')




    '''
    TRIGGER
    '''

    def TriggerEntity(self, entity):
        if entity.dash_action.trigger == 'start':
            self.TriggerEntityStart(entity)

        elif entity.dash_action.trigger == 'stop':
            self.TriggerEntityStop(entity)

    def TriggerEntityStart(self, entity):
        entity.dash_action.trigger_status = 'none'

        entity.dash_action.active_status = 'active'
        entity.dash_action.timer = 0

    def TriggerEntityStop(self, entity):
        entity.dash_action.trigger_status = 'none'

        entity.dash_action.active_status = 'inactive'
        entity.dash_action.cooldown_timer = 0





    '''
    Process actions
    '''


    def ProcessAction(self, entity, world, dt):

        # Active
        if entity.dash_action.active_status == 'active':

            # Check timer
            if entity.dash_action.timer >= entity.dash_action.period:
                self.StopAction(entity)
                return


            # Complete the action
            if self.CheckDashValid(entity):
                self.Dash(entity)
                self.UpdateTimer(entity, dt)
                pass

            # Action invalid; stop
            else:
                self.StopAction(entity)



        # Inactive
        elif entity.dash_action.active_status == 'inactive':
            pass



    def Dash(self, entity):
        if entity.dash_action.direction == 'left':
            vx_target = -entity.dash_action.speed()
            ax = -constants.infinity
            x_source = kinematics_component.KinematicsXSource(ax, vx_target)
            entity.kinematics.x_sources.append(x_source)

        elif entity.dash_action.direction == 'right':
            vx_target = entity.dash_action.speed()
            ax = constants.infinity
            x_source = kinematics_component.KinematicsXSource(ax, vx_target)
            entity.kinematics.x_sources.append(x_source)



    def CheckDashValid(self, entity):
        if entity.gravity.grounded == True:
            return True

        else:
            return False



    def UpdateTimer(self, entity, dt):
        entity.dash_action.timer += dt
