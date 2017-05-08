import sdl2

class ControllerInputSystem:
    def __init__(self):
        pass

    def HandleInput(self, input, world):
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
