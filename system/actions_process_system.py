


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
        self.action_map['RunLeft'] = self.RunLeft
        pass

    def ProcessActions(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.actions != None:
                for action in entity.actions.action_queue:
                    '''
                    if action == 'RunLeft':
                        self.MoveLeft(entity)

                    elif action == 'RunRight':
                        self.MoveRight(entity)

                    elif action == 'MoveUp':
                        self.MoveUp(entity)

                    elif action == 'MoveDown':
                        self.MoveDown(entity)

                    elif action == 'MoveHorizontalStop':
                        self.MoveHorizontalStop(entity)

                    elif action == 'MoveVerticalStop':
                        self.MoveVerticalStop(entity)

                    elif action == 'Stop':
                        self.Stop(entity)

                    elif action == 'Jump':
                        self.Jump(entity)
                    '''

                    self.action_map[action](entity)

                self.ClearEntityActions(entity)

    def ClearEntityActions(self, entity):
        entity.actions.action_queue = []



    def MoveLeft(self, entity):
        xspeed = entity.velocity.xspeed
        entity.velocity.vx = -1*xspeed
        if entity.orientation != None:
            entity.orientation.facing = 'left'

    def MoveRight(self, entity):
        xspeed = entity.velocity.xspeed
        entity.velocity.vx = xspeed
        if entity.orientation != None:
            entity.orientation.facing = 'right'

    def MoveUp(self, entity):
        yspeed = entity.velocity.yspeed
        entity.velocity.vy = -1*yspeed

    def MoveDown(self, entity):
        yspeed = entity.velocity.yspeed
        entity.velocity.vy = yspeed

    def MoveHorizontalStop(self, entity):
        entity.velocity.vx = 0

    def MoveVerticalStop(self, entity):
        entity.velocity.vy = 0

    def Stop(self, entity):
        entity.velocity.vx = 0

    def Jump(self, entity):
        if entity.gravity.grounded == True:
            entity.vy = entity.jump.speed
