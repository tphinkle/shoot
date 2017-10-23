class ActionsComponent():
    def __init__(self):

        # Stores the actual actions
        self.actions_list = []

        # Stores proposed commands
        self.raw_commands = []
        self.commands = []


        # Add specific actions that will interrupt or override others
        self.action_overrides = {}
        self.action_interrupts = {}
