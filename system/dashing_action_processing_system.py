# Python standard library
import sys


# Game specific
sys.path.append('../component/')
import kinematics_component

sys.path.append('../functions/')
import constants

import helper_systems



class DashingActionProcessingSystem(helper_systems.Subject):

    def __init__(self):

        # Initialize observer class
        helper_systems.Subject.__init__(self)

    def InterpretRawCommand(self, entity, raw_proposed_action):
        if raw_proposed_action['action'] == 'dash' and raw_proposed_action['trigger'] == 'start':
            direction = entity.orientation.xorientation

        return 'dash' + direction


    def Trigger(self, entity, action):
        if action['trigger'] == 'start':
            self.StartAction(entity, action)
        elif action['trigger'] == 'stop':
            self.StopAction(entity)

    def StartAction(self, entity, action):
        entity.dashing_action.status = 'active'

        if entity.orientation.xorientation == 'left':
            entity.dashing_action.direction = 'left'


        elif entity.orientation.xorientation == 'right':
            entity.dashing_action.direction = 'right'



    def StopAction(self, entity):
        entity.dashing_action.status = 'inactive'
        entity.dashing_action.timer = 0





    def ProcessAction(self, entity, world, dt):
        for key, entity in world.entity_manager.entities.iteritems():
            if entity.dashing_action:



                # Active
                if entity.dashing_action.status == 'active':

                    # Check timer
                    if entity.dashing_action.timer >= entity.dashing_action.period:
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
                elif entity.dashing_action.status == 'inactive':
                    pass



    def Dash(self, entity):
        if entity.dashing_action.direction == 'left':
            vx_target = -entity.dashing_action.speed()
            ax = -constants.infinity
            x_source = kinematics_component.KinematicsXSource(ax, vx_target)
            entity.kinematics.x_sources.append(x_source)

        elif entity.dashing_action.direction == 'right':
            vx_target = entity.dashing_action.speed()
            ax = constants.infinity
            x_source = kinematics_component.KinematicsXSource(ax, vx_target)
            entity.kinematics.x_sources.append(x_source)



    def CheckDashValid(self, entity):
        if entity.gravity.grounded == True:
            return True

        else:
            return False



    def UpdateTimer(self, entity, dt):
        entity.dashing_action.timer += dt
