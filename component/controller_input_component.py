class ControllerInputComponent():
    def __init__(self):
        self.action_mapping = {}
        self.action_mapping['Left'] = 'MoveLeft'
        self.action_mapping['Right'] = 'MoveRight'
        self.action_mapping['Up'] = 'Up'
        self.action_mapping['Down'] = 'Down'
        self.action_mapping['B'] = 'Jump'
        self.action_mapping['Y'] = 'Shoot'
        self.action_mapping['A'] = 'Dash'
