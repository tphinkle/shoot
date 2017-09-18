class ActionsProcessingSystem():
    '''
    * Action processing pipeline:
        0. Create/Register
            - e.g., create action from controller input
            - e.g., create action from AI input
        1. Validate
            - Check if action is permissable; if not, filter out
        2. Sort
            - Sort actions so they are processed in correct order
        3. Process
            - Perform the action

    * Final step in the action processing pipeline

    * Enacts the proposed actions

    * Appends the proposed action to the entity's action state

    '''

    def __init__(self):
        self.action_process_map = {}




        '''
        Panning
        e.g. for cameras
        '''

        self.action_process_map['PanLeft'] = self.ProcessPanLeft
        self.action_process_map['PanRight'] = self.ProcessPanRight
        self.action_process_map['PanUp'] = self.ProcessPanUp
        self.action_process_map['PanDown'] = self.ProcessPanDown
        self.action_process_map['PanHorizontalStop'] = self.ProcessPanHorizontalStop
        self.action_process_map['PanVerticalStop'] = self.ProcessPanVerticalStop


        '''
        Horizontal movement
        '''
        self.action_process_map['MoveLeft'] = self.ProcessMoveLeft
        self.action_process_map['MoveRight'] = self.ProcessMoveRight
        self.action_process_map['MoveStop'] = self.ProcessMoveHorizontalStop


        '''
        Jumping
        '''
        self.action_process_map['Jump'] = self.ProcessJump



        '''
        Shoot Buster
        '''
        self.action_process_map['Shoot'] = self.ProcessShootBuster



    def ProcessActions(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.actions != None:
                for action in entity.actions.action_queue:
                    self.action_process_map[action](entity)

                self.ClearEntityActions(entity)

    def ClearEntityActions(self, entity):
        entity.actions.action_queue = []


    '''
    Running actions
    '''


    def ProcessMoveLeft(self, entity):
        entity.velocity.vx = -1*entity.running_action.speed


    def ProcessMoveRight(self, entity):
        entity.velocity.vx = entity.running_action.speed


    def ProcessMoveHorizontalStop(self, entity):
        entity.velocity.vx = 0



    '''
    Panning actions
    '''

    def ProcessPanLeft(self, entity):
        entity.velocity.vx = -1*entity.panning_action.xspeed

    def ProcessPanRight(self, entity):
        entity.velocity.vx = entity.panning_action.xspeed

    def ProcessPanUp(self, entity):
        entity.velocity.vy = -1*entity.panning_action.yspeed

    def ProcessPanDown(self, entity):
        entity.velocity.vy = entity.panning_action.yspeed

    def ProcessPanHorizontalStop(self, entity):
        entity.velocity.vx = 0

    def ProcessPanVerticalStop(self, entity):
        entity.velocity.vy = 0

    '''
    Jumping actions
    '''

    def ProcessJump(self, entity):
        entity.velocity.vy = -1*entity.jumping_action.speed


    '''
    Buster actions
    '''

    def ProcessShootBuster(self, entity):
        #if entity.
        pass

    def ProcessChargeBuster(self, entity):
        pass
