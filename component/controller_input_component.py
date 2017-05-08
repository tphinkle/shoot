class ControllerInputComponent():
    def __init__(self):
        self.action_mapping = {}
        self.action_mapping['Left'] = 'MoveLeft'
        self.action_mapping['Right'] = 'MoveRight'
        self.action_mapping['Null'] = 'Stop'
        self.action_mapping['B'] = 'Jump'
        self.action_mapping['Y'] = 'Shoot'
