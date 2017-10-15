# Python standard library
import sys

# Game specific
sys.path.append('../component/')
import kinematics_component

sys.path.append('../functions/')
import constants


class JumpingActionProcessingSystem(object):

    def __init__(self):
        pass




    def Trigger(self, entity, action):
        if action['trigger'] == 'start':
            self.StartAction(entity, action)
        elif action['trigger'] == 'stop':
            self.StopAction(entity)

    def StartAction(self, entity, action):

        # Single jump
        if entity.gravity.grounded == True:

            # Set jumping active and single jump mode
            entity.jumping_action.status = 'active'
            entity.jumping_action.mode = 'single'


            # Give initial speed boost
            ay = -constants.infinity
            target_vy = -entity.jumping_action.initial_speed

            y_source = kinematics_component.KinematicsYSource(ay, target_vy)
            entity.kinematics.y_sources.append(y_source)

        # Double jump
        elif entity.jumping_action.double_jump_available == True:
            entity.jumping_action.status = 'active'
            entity.jumping_action.mode = 'double'
            entity.jumping_action.double_jump_available = False

    def StopAction(self, entity):
        entity.jumping_action.status = 'inactive'
        entity.jumping_action.timer = 0






    def ProcessAction(self, world, dt):
        for key, entity in world.entity_manager.entities.iteritems():
            if entity.jumping_action:



                # Active
                if entity.jumping_action.status == 'active':

                    # Single jump
                    if entity.jumping_action.mode == 'single':

                        # Check timer
                        if entity.jumping_action.timer >= entity.jumping_action.period:
                            self.StopAction(entity)
                            return

                        self.SingleJump(entity)



                    # Double jump
                    elif entity.jumping_action.mode == 'double':
                        # Check timer
                        if entity.jumping_action.timer >= entity.jumping_action.period:
                            self.StopAction(entity)
                            return

                        self.DoubleJump(entity)

                    self.UpdateTimer(entity, dt)


                # Inactive
                elif entity.jumping_action.status == 'inactive':
                    if entity.gravity.grounded == True:
                        entity.jumping_action.double_jump_available = True
                    pass


    def SingleJump(self, entity):


        ay = -entity.jumping_action.acceleration*2.25
        target_vy = -999999999

        y_source = kinematics_component.KinematicsYSource(ay, target_vy)
        entity.kinematics.y_sources.append(y_source)




    def DoubleJump(self, entity):
        # Give initial speed boost
        ay = -constants.infinity
        target_vy = -entity.jumping_action.initial_speed

        y_source = kinematics_component.KinematicsYSource(ay, target_vy)
        entity.kinematics.y_sources.append(y_source)




    def UpdateTimer(self, entity, dt):
        entity.jumping_action.timer += dt
