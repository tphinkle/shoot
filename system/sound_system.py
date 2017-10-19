# Python standard library

# sdl
import sdl2.sdlmixer



class SoundSystem(object):
    '''
    Notes:
        - https://www.libsdl.org/projects/SDL_mixer/docs/SDL_mixer.html#SEC10
        - http://lazyfoo.net/SDL_tutorials/lesson11/index.php
    '''


    def __init__(self):
        self.song = None
        self.playing = False

        pass


    def PlaySounds(self, world, dt):
        if self.playing == False:
            song_file_path = world.song_file_path

            music = sdl2.sdlmixer.Mix_LoadWAV(song_file_path)
            #print sdl2.sdlmixer.Mix_PlayMusic(music, -1)

            #print sdl2.sdlmixer.Mix_FadeInChannelTimed(-1, music, 0, 100, 1)
            sdl2.sdlmixer.Mix_PlayChannel(-1, music, 0)


            #print sdl2.sdlmixer.Mix_GetError()
        self.playing = True
