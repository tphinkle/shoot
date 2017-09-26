



class ActionsValidationSystem:

    '''
    * Action processing pipeline:
        0. Create/Register
            - e.g., create action from controller input
            - e.g., create action from AI input
        1. Validate
            - Check if action is permissable; if not, filter out
            - Check context so generic actions are mapped onto correct
            context-specific action
                - e.g., MoveLeft->FloatLeft or RunLeft depending on context
        2. Sort
            - Sort actions so they are processed in correct order
        3. Process
            - Perform the action

    * Second step in the action processing pipeline.

    * Checks whether a proposed action is permitted
        - e.g., check if entity is stunned before allowing action
        - e.g., check if entity is grounded if entity attempts to jump

    * If action allowed, continue; else, remove from action list

    * End result is a filtered entity action list
    '''

    def __init__(self):
        self.action_validate_map = {}

        '''
        Panning
        e.g. for cameras
        '''

        self.action_validate_map['PanLeft'] = self.ValidatePanLeft
        self.action_validate_map['PanRight'] = self.ValidatePanRight
        self.action_validate_map['PanUp'] = self.ValidatePanUp
        self.action_validate_map['PanDown'] = self.ValidatePanDown
        self.action_validate_map['PanHorizontalStop'] = self.ValidatePanHorizontalStop
        self.action_validate_map['PanVerticalStop'] = self.ValidatePanVerticalStop

        '''
        Horizontal movement
        '''
        self.action_validate_map['MoveLeft'] = self.ValidateMoveLeft
        self.action_validate_map['MoveRight'] = self.ValidateMoveRight
        self.action_validate_map['MoveStop'] = self.ValidateMoveStop

        '''
        Jumping
        '''
        self.action_validate_map['Jump'] = self.ValidateJump


        '''
        Shoot Buster
        '''
        self.action_validate_map['Shoot'] = self.ValidateShoot

        pass




    def ValidateActions(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.actions != None:
                for action in entity.actions.action_queue:
                    self.action_validate_map[action](entity)


    def ValidatePanLeft(self, entity):
        pass


    def ValidatePanRight(self, entity):
        pass


    def ValidatePanUp(self, entity):
        pass


    def ValidatePanDown(self, entity):
        pass


    def ValidatePanHorizontalStop(self, entity):
        pass


    def ValidatePanVerticalStop(self, entity):
        pass


    def ValidateMoveLeft(self, entity):
        pass


    def ValidateMoveRight(self, entity):
        pass


    def ValidateMoveStop(self, entity):
        pass


    def ValidateJump(self, entity):
        pass


    def ValidateShoot(self, entity):
        pass
