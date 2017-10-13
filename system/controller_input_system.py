# Python standard library
import copy

# SDL related
import sdl2

class ControllerInputSystem:

    def __init__(self, joystick):
        self.joystick_current = None
        self.joystick_previous = None

        self.x_current = sdl2.SDL_JoystickGetAxis(joystick, 0)
        self.x_previous = sdl2.SDL_JoystickGetAxis(joystick, 0)

        self.y_current = sdl2.SDL_JoystickGetAxis(joystick, 1)
        self.y_previous = sdl2.SDL_JoystickGetAxis(joystick, 1)





    def HandleInputEventDriven(self, joystick, inputs, world):

        #self.UpdateJoystick(joystick)
        self.UpdateDPad(joystick)

        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.controller_input != None:
                buttons = []


                # Joystick
                for input in inputs:

                    '''
                    Buttons
                    '''

                    # Button pressed
                    if (input.type == sdl2.SDL_JOYBUTTONDOWN):

                        if input.jbutton.button == 0:
                            buttons.append('A_Press')

                        elif input.jbutton.button == 1:
                            buttons.append('B_Press')

                        elif input.jbutton.button == 3:
                            buttons.append('Y_Press')

                    # Button released
                    elif (input.type == sdl2.SDL_JOYBUTTONUP):

                        if input.jbutton.button == 0:
                            buttons.append('A_Release')

                        elif input.jbutton.button == 1:
                            buttons.append('B_Release')

                        elif input.jbutton.button == 3:
                            buttons.append('Y_Release')


                if self.x_previous < 100 and self.x_current > 100:
                    buttons.append('Right_Press')
                elif self.x_previous > -100 and self.x_current < -100:
                    buttons.append('Left_Press')
                elif abs(self.x_previous) > 100 and abs(self.x_current) < 100:
                    buttons.append('LeftRight_Release')




                # Convert button presses into proposed actions
                for button in buttons:
                    actions = entity.controller_input.action_mapping[button]
                    for action in actions:
                        entity.actions.proposed_actions.append(action)


    def UpdateDPad(self, joystick):
        self.x_previous = self.x_current
        self.x_current = sdl2.SDL_JoystickGetAxis(joystick, 0)










    '''
    def HandleInputJoystickStateDriven(self, joystick, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.controller_input != None:



                buttons = []

                # Check input

                left_right = sdl2.SDL_JoystickGetAxis(joystick, 0)
                if left_right < 0:
                    buttons.append('Left')
                elif left_right > 0:
                    buttons.append('Right')

                up_down = sdl2.SDL_JoystickGetAxis(joystick, 1)

                button_1 = sdl2.SDL_JoystickGetButton(joystick, 1)
                if button_1 == 1:
                    buttons.append('B')

                button_0 = sdl2.SDL_JoystickGetButton(joystick, 0)
                if button_0 == 1:
                    buttons.append('A')



                # Get proposed actions

                for button in buttons:
                    action = entity.controller_input.action_mapping[button]
                    entity.actions.proposed_actions.append(action)
    '''
