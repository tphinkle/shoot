class ControllerInputComponent():
    def __init__(self):
        self.action_mapping = {}
        self.action_mapping['Left_Press'] = [{'action':'move', 'trigger':'start', 'direction': 'left'}]
        self.action_mapping['Right_Press'] = [{'action':'move', 'trigger':'start', 'direction': 'right'}]

        self.action_mapping['B_Press'] = [{'action': 'jump', 'trigger':'start'}]
        self.action_mapping['Y_Press'] = [{'action':'shoot', 'trigger':'start', 'gun':'buster'},
        {'action': 'shoot', 'trigger':'start', 'gun':'charge_buster'}]
        self.action_mapping['A_Press'] = [{'action':'dash', 'trigger': 'start'}]

        self.action_mapping['LeftRight_Release'] = [{'action':'move', 'trigger':'stop'}]
        self.action_mapping['B_Release'] = [{'action': 'jump', 'trigger':'stop'}]
        self.action_mapping['Y_Release'] = [{'action':'shoot', 'trigger':'stop', 'gun':'buster'}]
        self.action_mapping['A_Release'] = [{'action':'dash', 'trigger': 'stop'}]
