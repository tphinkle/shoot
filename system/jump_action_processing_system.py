# Python standard library
import sys

# Game specific
sys.path.append('../component/')
import kinematics_component

sys.path.append('../functions/')
import constants

import helper_systems


class JumpActionProcessingSystem(helper_systems.Subject):

    def __init__(self):


        # Initialize observer class
        helper_systems.Subject.__init__(self)


    def SetEntityTrigger(self, entity, command):
        if command['trigger'] == 'start':

            # start OK
            if CheckStartTriggerConditions(entity, command):
                entity.jump_action.trigger_status = 'start'

            # start not OK
            else:
                entity.jump_action.trigger_status = 'none'

        elif command['trigger'] == 'stop':

            # stop OK
            if CheckStopTriggerConditions(entity, command):
                entity.jump_action.trigger_status = 'stop'

            # stop not OK
            else:
                entity.jump_action.trigger_status = 'none'

    def CheckStartTriggerConditions(self, entity, command):
        return ((entity.jump_action.active_status == 'inactive')
            and (entity.gravity.grounded == True))


    def CheckStopTriggerConditions(self, entity, command):
        return (entity.jump_action.active_status == 'active')



    def Trigger(self, entity, action):
        if action['trigger'] == 'start':
            self.TriggerStart(entity, action)
        elif action['trigger'] == 'stop':
            self.TriggerStop(entity)

    def TriggerStart(self, entity, action):

        # Set jump active and single jump mode
        entity.jump_action.active_status = 'active'
        entity.jump_action.mode = 'single'


        # Give initial speed boost
        ay = -constants.infinity
        target_vy = -entity.jump_action.initial_speed

        y_source = kinematics_component.KinematicsYSource(ay, target_vy)
        entity.kinematics.y_sources.append(y_source)

        # Double jump
        elif entity.jump_action.double_jump_available == True:
            entity.jump_action.active_status = 'active'
            entity.jump_action.mode = 'double'
            entity.jump_action.double_jump_available = False

    def TriggerStop(self, entity):
        entity.jump_action.active_status = 'inactive'
        entity.jump_action.timer = 0






    def ProcessAction(self, entity, world, dt):

        # Active
        if entity.jump_action.active_status == 'active':

            # Single jump
            if entity.jump_action.mode == 'single':

                # Check timer
                if entity.jump_action.timer >= entity.jump_action.period:
                    self.StopAction(entity)
                    return

                self.SingleJump(entity)



            # Double jump
            elif entity.jump_action.mode == 'double':
                # Check timer
                if entity.jump_action.timer >= entity.jump_action.period:
                    self.StopAction(entity)
                    return

                self.DoubleJump(entity)

            self.UpdateTimer(entity, dt)


        # Inactive
        elif entity.jump_action.active_status == 'inactive':
            if entity.gravity.grounded == True:
                entity.jump_action.double_jump_available = True
            pass


    def SingleJump(self, entity):


        ay = -entity.jump_action.acceleration*2.25
        target_vy = -999999999

        y_source = kinematics_component.KinematicsYSource(ay, target_vy)
        entity.kinematics.y_sources.append(y_source)




    def DoubleJump(self, entity):
        # Give initial speed boost
        ay = -constants.infinity
        target_vy = -entity.jump_action.initial_speed

        y_source = kinematics_component.KinematicsYSource(ay, target_vy)
        entity.kinematics.y_sources.append(y_source)




    def UpdateTimer(self, entity, dt):
        entity.jump_action.timer += dt
