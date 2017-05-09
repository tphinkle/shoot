class ActionsProcessSystem():
    '''
    Converts a proposed action (as determined by controller input or AI) into
    its proper output.

    Validation occurs in this class for now (for instance, if hero has max
    number of bullets out and tries to shoot, validation here will prevent
    another shot from being made).
    '''

    def __init__(self):
        self.action_map = {}

        # Running
        self.action_map['RunLeft'] = self.RunLeft
        self.action_map['RunRight'] = self.RunRight
        self.action_map['RunStop'] = self.RunStop

        # Panning
        self.action_map['PanLeft'] = self.PanLeft
        self.action_map['PanRight'] = self.PanRight
        self.action_map['PanUp'] = self.PanUp
        self.action_map['PanDown'] = self.PanDown
        self.action_map['PanHorizontalStop'] = self.PanHorizontalStop
        self.action_map['PanVerticalStop'] = self.PanVerticalStop

        # Jumping
        self.action_map['Jump'] = self.Jump



    def ProcessActions(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.actions != None:
                for action in entity.actions.action_queue:
                    self.action_map[action](entity)

                self.ClearEntityActions(entity)

    def ClearEntityActions(self, entity):
        entity.actions.action_queue = []


    '''
    Running actions
    '''

    def RunLeft(self, entity):
        entity.velocity.vx = -1*entity.running_action.speed


    def RunRight(self, entity):
        entity.velocity.vx = entity.running_action.speed


    def RunStop(self, entity):
        entity.velocity.vx = 0

    '''
    Panning actions
    '''

    def PanLeft(self, entity):
        entity.velocity.vx = -1*entity.panning_action.xspeed

    def PanRight(self, entity):
        entity.velocity.vx = entity.panning_action.xspeed

    def PanUp(self, entity):
        entity.velocity.vy = -1*entity.panning_action.yspeed

    def PanDown(self, entity):
        entity.velocity.vy = entity.panning_action.yspeed

    def PanHorizontalStop(self, entity):
        entity.velocity.vx = 0

    def PanVerticalStop(self, entity):
        entity.velocity.vy = 0

    '''
    Jumping actions
    '''

    def Jump(self, entity):
        if entity.gravity.grounded == True:
            entity.velocity.vy = -1*entity.jumping_action.speed
