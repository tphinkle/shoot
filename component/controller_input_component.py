class ControllerInputComponent():
    def __init__(self):
        self.action_mapping = {}
        self.action_mapping['Left_Press'] = ['move', ['start', 'left']]
        self.action_mapping['Right_Press'] = ['move', ['start', 'right']]
        self.action_mapping['Up_Press'] = ['up', ['start']]
        self.action_mapping['Down_Press'] = ['down', ['start']]
        self.action_mapping['B_Press'] = ['jump', ['start']]
        self.action_mapping['Y_Press'] = ['shoot', ['start']]
        self.action_mapping['A_Press'] = ['dash', ['start']]

        self.action_mapping['LeftRight_Release'] = ['move', ['stop']]
        self.action_mapping['UpDown_Release'] = ['updown', ['stop']]
        self.action_mapping['B_Release'] = ['jump', ['stop']]
        self.action_mapping['Y_Release'] = ['shoot', ['stop']]
        self.action_mapping['A_Release'] = ['dash', ['stop']]
