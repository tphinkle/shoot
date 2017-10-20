# Python standard library
import sys
import ctypes

# sdl
import sdl2.sdlmixer

# Program specific
sys.path.append('../component')
import kinematics_component

sys.path.append('../functions')
import coord_transforms



class SoundSystem(object):
    '''
    Notes:
        - https://www.libsdl.org/projects/SDL_mixer/docs/SDL_mixer.html#SEC10
        - http://lazyfoo.net/SDL_tutorials/lesson11/index.php
    '''


    def __init__(self):
        self.num_playing = 0

        distance = 3
        self.left_mic = Microphone(distance)
        self.right_mic = Microphone(distance)

        pass





    def Update(self, world, dt):
        self.UpdateMicPosition(world)
        self.PlayRoomMusic(world, dt)


        if self.playing == False:
            song_file_path = world.song_file_path

            music = sdl2.sdlmixer.Mix_LoadWAV(song_file_path)
            #print sdl2.sdlmixer.Mix_PlayMusic(music, -1)

            #print sdl2.sdlmixer.Mix_FadeInChannelTimed(-1, music, 0, 100, 1)
            sdl2.sdlmixer.Mix_PlayChannel(-1, music, 0)


            #print sdl2.sdlmixer.Mix_GetError()
        self.playing = True

    def PlayRoomMusic(self, world, dt):
        sound = world.room.sound.sound_queue[0]

        if sound.playing == True:
            pass

        elif sound.playing == False:
            self.StartSound(sound)



    def StartSound(self, sound):

        # Get the sound's file path
        file_path = sound.file_path

        # Load the wav file
        mix_chunk = sdl2.sdlmixer.Mix_LoadWAV(file_path)

        # Attach end of play to mix channel
        self.num_playing += 1






        
        # Create callback function
        callback_types = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
        def OnStopPlaying(channel):
            self.num_playing -= 1
            print self.num_playing
            return 0

        callback_function = callback_types(OnStopPlaying)
        sdl2.sdlmixer.Mix_ChannelFinished(callback_function)






        # Play the channel
        channel = sdl2.sdlmixer.Mix_PlayChannel(-1, mix_chunk, 0)

        # Set the sound parameter info
        sound.channel = channel
        sound.playing = True


    def StopSound(self, world, dt):

        pass



    def UpdateMicPosition(self, world):
        camera = world.entity_manager.entities['camera_0']

        camera_center_pixel = coord_transforms.GetEntityMiddleCenterPixel(camera)
        camera_center_x = camera_center_pixel[0]
        camera_center_y = camera_center_pixel[1]

        self.left_mic.kinematics.x = camera_center_x - self.left_mic.distance
        self.left_mic.kinematics.y = camera_center_y

        self.right_mic.kinematics.x = camera_center_x + self.right_mic.distance
        self.right_mic.kinematics.y = camera_center_y




class Microphone(object):
    def __init__(self, distance):
        self.distance = distance
        self.kinematics = kinematics_component.KinematicsComponent()
