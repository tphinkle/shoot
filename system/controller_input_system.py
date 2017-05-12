import sdl2

class ControllerInputSystem:
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
                elif left_right == 0:
                    buttons.append('Null')

                up_down = sdl2.SDL_JoystickGetAxis(joystick, 1)

                # Buttons
                button_1 = sdl2.SDL_JoystickGetButton(joystick, 1)
                if button_1 == 1:
                    buttons.append('B')

                for button in buttons:
                    action = entity.controller_input.action_mapping[button]
                    entity.actions.action_queue.append(action)



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
                        elif input.jaxis.value == 0:
                            buttons.append('Null')

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

                elif (input.type == sdl2.SDL_KEYUP):
                    buttons.append('Null')



                for button in buttons:
                    self.AppendActionToEntityActionQueue(entity, button)



    def AppendActionToEntityActionQueue(self, entity, button):
        action = entity.controller_input.action_mapping[button]
        entity.actions.action_queue.append(action)
