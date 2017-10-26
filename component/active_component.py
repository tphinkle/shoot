class ActiveComponent():
    def __init__(self):

        # Stores the actual actions
        self.actions = []

        # Stores proposed commands
        self.commands = []



class Action(object):
    def __init__(self, action_class, action_name):
        self.action_class = action_class
        self.action_name = action_name
        self.active_status = None
        self.trigger_status = None


        
