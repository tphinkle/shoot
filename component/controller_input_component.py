class ControllerInputComponent():
    def __init__(self):
        self.action_mapping = {}
        self.action_mapping['Left'] = 'RunLeft'
        self.action_mapping['Right'] = 'RunRight'
        self.action_mapping['Null'] = 'RunStop'
        self.action_mapping['B'] = 'Jump'
        self.action_mapping['Y'] = 'Shoot'
