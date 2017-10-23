class ControllerInputComponent():
    def __init__(self):
        self.action_mapping = {}
        # Movement class
        # Needs class, action, and trigger
        self.action_mapping['Left_Press'] = [{'class':'move', 'action':'moveleft', 'trigger':'start'}]
        self.action_mapping['Right_Press'] = [{'class':'move', 'action':'moveright', 'trigger':'start'}]
        self.action_mapping['LeftRight_Release'] = [{'class':'move', 'action':'move', 'trigger':'stop'}]


        # Shooting class
        # Needs class, action, gun, and trigger
        self.action_mapping['Y_Press'] = [{'class':'shoot', 'action':'shoot', 'gun':'buster', 'trigger':'start'},
        {'class': 'shoot', 'action':'charge', 'gun':'charge_buster', 'trigger':'start'}]
        self.action_mapping['Y_Release'] = [{'class':'shoot', 'trigger':'stop', 'gun':'charge_buster'},
         {'class':'shoot', 'trigger':'stop', 'gun':'buster'}]




        # Dashing class
        # Need class, trigger
        self.action_mapping['A_Press'] = [{'class':'dash', 'trigger': 'start'}]
        self.action_mapping['A_Release'] = [{'class':'dash', 'trigger': 'stop'}]




        # Jumping class
        # Needs trigger, start, stop
        self.action_mapping['B_Press'] = [{'class': 'jump', 'action':'jump', 'trigger':'start'},
        {'class': 'jump', 'action':'airjump', 'trigger':'start'}]
        self.action_mapping['B_Release'] = [{'class': 'jump', 'action':'jump', 'trigger':'stop'},
        {'class': 'jump', 'action':'airjump', 'trigger':'stop'}]
