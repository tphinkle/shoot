# Python standard library
import sys


# Game specific
sys.path.append('../component/')
import kinematics_component

sys.path.append('../functions/')
import constants



class DashingActionProcessingSystem(object):

    def __init__(self):
        pass



    def Trigger(self, entity, args):
        if 'start' in args:
            self.StartAction(entity, args)
        elif 'stop' in args:
            self.StopAction(entity, args)

    def StartAction(self, entity, args):
        entity.dashing_action.status = 'active'

        if entity.orientation.facing == 'left':
            entity.dashing_action.direction = 'left'


        elif entity.orientation.facing == 'right':
            entity.dashing_action.direction = 'right'



    def StopAction(self, entity, args = None):
        entity.dashing_action.status = 'inactive'
        entity.dashing_action.timer = 0





    def ProcessAction(self, world, dt):
        for key, entity in world.entity_manager.entitys.iteritems():
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
