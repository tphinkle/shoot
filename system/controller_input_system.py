# SDL related
import sdl2

class ControllerInputSystem:

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


    * First step in action processing pipeline (parallel w/ AI)

    * Reads the controller state using sdl2

    * Converts the controllers state into an action, which is mapped via the
    entity's ControllerInput component

    * Adds the action onto the entity's entity.action.action_queue

    '''



    def __init__(self):
        pass

    def HandleInputJoystickStateDriven(self, joystick, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.controller_input != None:
                buttons = []

                # Check dpad
                left_right = sdl2.SDL_JoystickGetAxis(joystick, 0)
                if left_right < 0:
                    buttons.append('Left')
                elif left_right > 0:
                    buttons.append('Right')
                #elif left_right == 0:
                    #buttons.append('Null')

                up_down = sdl2.SDL_JoystickGetAxis(joystick, 1)

                # Buttons
                button_1 = sdl2.SDL_JoystickGetButton(joystick, 1)
                if button_1 == 1:
                    buttons.append('B')

                button_0 = sdl2.SDL_JoystickGetButton(joystick, 0)
                if button_0 == 1:
                    buttons.append('A')

                for button in buttons:
                    action = entity.controller_input.action_mapping[button]
                    entity.actions.proposed_actions.append(action)



    def HandleInputEventDriven(self, input, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.controller_input != None:
                buttons = []



                '''
                Joystick
                '''
                if (input.type == sdl2.SDL_JOYBUTTONDOWN):
                    if input.jbutton.button == 1:
                        buttons.append('B')

                    if input.jbutton.button == 3:
                        buttons.append('Y')

                elif (input.type == sdl2.SDL_JOYAXISMOTION):
                    if input.jaxis.axis == 0:
                        if input.jaxis.value < 0:
                            print 'left!'
                            buttons.append('Left')
                        elif input.jaxis.value > 0:
                            buttons.append('Right')

                        # Old function when not pressing left or right was a command
                        #elif input.jaxis.value == 0:
                            #buttons.append('Null')

                    if input.jaxis.axis == 1:
                        if input.jaxis.value < 0:
                            pass
                        if input.jaxis.value > 0:
                            pass

                '''
                Keyboard
                '''

                if (input.type == sdl2.SDL_KEYDOWN):

                    if input.key.keysym.scancode == 80:
                        buttons.append('Left')

                    elif input.key.keysym.scancode == 79:
                        buttons.append('Right')

                    if input.key.keysym.scancode == 82:
                        buttons.append('B')

                #elif (input.type == sdl2.SDL_KEYUP):
                    #buttons.append('Null')



                for button in buttons:
                    self.AppendActionToEntityActionQueue(entity, button)



    def AppendActionToEntityActionQueue(self, entity, button):
        action = entity.controller_input.action_mapping[button]
        entity.actions.action_queue.append(action)
