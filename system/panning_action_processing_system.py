class PanningActionProcessingSystem():

    def __init__(self):

        pass


    def Trigger(self, entity, action):

        if action['trigger'] == 'start':
            self.StartAction(entity, action)

        elif action['trigger'] == 'stop':
            self.StopAction(entity, action)


        pass

    def StartAction(self, entity, action):
        entity.panning_action.status = 'active'


        if action['xdirection'] == 'left':
            entity.panning_action.xdirection = 'left'

        if action['xdirection'] == 'right':
            entity.panning_action.xdirection = 'right'

        else:
            entity.panning_action.xdirection = 'none'

        if action['ydirection'] == 'down':
            entity.panning_action.ydirection = 'down'

        elif action['ydirection'] == 'up':
            entity.panning_action.ydirection = 'up'

        else:
            entity.panning_action.ydirection = 'none'


    def StopAction(self, entity, action):
        entity.kinematics.vx = 0
        entity.kinematics.vy = 0
        entity.panning_action.status = 'inactive'





    def ProcessAction(self, world, dt):
        for key, entity in world.entity_manager.entities.iteritems():
            if entity.panning_action:

                # Active
                if entity.panning_action.status == 'active':
                    self.Pan(entity)



                # Inactive
                elif entity.panning_action.status == 'inactive':
                    pass




    def Pan(self, entity):

        # Pan left right
        if entity.panning_action.xdirection == 'left':
            entity.kinematics.vx_sources['panning'] = -entity.panning_action.xspeed

        elif entity.panning_action.xdirection == 'right':
            entity.kinematics.vx_sources['panning'] = entity.panning_action.xspeed

        # Pan up down
        if entity.panning_action.ydirection == 'up':
            entity.kinematics.vy_sources['panning'] = -entity.panning_action.yspeed

        elif entity.panning_action.ydirection == 'down':
            entity.kinematics.vy_sources['panning'] = entity.panning_action.yspeed
