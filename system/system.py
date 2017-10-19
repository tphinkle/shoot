# Standard library
import sys
import ctypes

# SDL
import sdl2
import sdl2.sdlimage
import sdl2.sdlttf
import sdl2.sdlmixer

###########
# Game
###########

# World
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/world/')
import world

# Entity
sys.path.append('../entity/')
import entity
import entity_manager

# Component

# System
import timer as timer
import render_system
import sound_system
import sprite_animation_system

import tile_modifier_system

import controller_input_system
import ai_system
import actions_processing_system


import factory_system



import friction_system
import gravity_system
import kinematics_system
import tilemap_collision_system





import status_processing_system







class System:
    def __init__(self):

        self.InitializeSDL()
        self.InitializeTimers()
        self.InitializeSubsystems()
        self.InitializeWorld()


    def InitializeSDL(self):
        # SDL sub systems
        sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)



        # Video
        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)


        # Window
        self.window = sdl2.SDL_CreateWindow("shoot 0.0.1",\
            sdl2.SDL_WINDOWPOS_UNDEFINED,\
            sdl2.SDL_WINDOWPOS_UNDEFINED,
            640,\
            480,\
            sdl2.SDL_WINDOW_SHOWN)

        # renderer
        self.sdl_renderer = sdl2.SDL_CreateRenderer(self.window, -1,\
            sdl2.SDL_RENDERER_ACCELERATED)
        sdl2.SDL_SetRenderDrawColor(self.sdl_renderer, 255, 255, 255, 0)

        # Sound (from tutorial: http://lazyfoo.net/SDL_tutorials/lesson11/index.php )
        # Initialize sdl mixer
        # Mix_OpenAudio args
        # First arg (22050) is sound frequency (recommended according to multiple tutorials,
        # but look into this)
        # Second arg is sound format
        # Third arg is number of channels we plan to use (e.g., 2 for stereo sound)
        # Fourth arg is the sample size (should be 4096)
        # Audio

        #sdl2.SDL_Init(sdl2.SDL_INIT_AUDIO)    # If using SDL sound; shouldn't do this

        sdl2.sdlmixer.Mix_Init(sdl2.sdlmixer.MIX_INIT_MOD)    # Insert the file formats you wish to allow here, e.g. OGG
        sdl2.sdlmixer.Mix_OpenAudio(22050, sdl2.sdlmixer.MIX_DEFAULT_FORMAT, 2, 4096)



        # TTF
        sdl2.sdlttf.TTF_Init()


        # Joystick
        sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK)
        self.joystick = sdl2.SDL_JoystickOpen(0)

        # Event
        self.input = sdl2.SDL_Event()


    def InitializeTimers(self):
        # Timers
        self.render_period = 1./60
        self.render_timer = timer.Timer(self.render_period)

        self.game_period = 1./240
        self.game_timer = timer.Timer(self.game_period)


    def InitializeSubsystems(self):
        # Systems
        self.sound_system = sound_system.SoundSystem()
        self.render_system = render_system.RenderSystem(self.sdl_renderer, self.window)
        self.sprite_animation_system = sprite_animation_system.SpriteAnimationSystem()


        # Actions systems
        self.controller_input_system = controller_input_system.ControllerInputSystem(self.joystick)
        self.actions_processing_system = actions_processing_system.ActionsProcessingSystem()



        self.tile_modifier_system = tile_modifier_system.TileModifierSystem()


        self.factory_system = factory_system.FactorySystem()



        self.kinematics_system = kinematics_system.KinematicsSystem()


        self.gravity_system = gravity_system.GravitySystem()
        self.friction_system = friction_system.FrictionSystem()
        self.ai_system = ai_system.AISystem()
        self.tilemap_collision_system = tilemap_collision_system.TilemapCollisionSystem()


        self.status_processing_system = status_processing_system.StatusProcessingSystem()

    def InitializeWorld(self):
        self.world = world.World()



    def LoadGame(self):
        self.world.LoadGame()


    def GetInputs(self):
        # Poll events
        inputs = []
        while sdl2.SDL_PollEvent(ctypes.byref(self.input)) != 0:
            inputs.append(self.input)
            if self.input.type == sdl2.SDL_QUIT:
                self.running = False
                break

            else:
                pass

        return inputs

    def Quit(self):

        # Quit mixer
        #print sdl2.sdlmixer.Mix_QuerySpec()
        sdl2.sdlmixer.Mix_CloseAudio()
        sdl2.sdlmixer.Mix_Quit()
        pass


    def Run(self):
        # Begin main loop
        self.LoadGame()
        self.running = True
        while self.running:

            # Game
            if self.game_timer.Update():






                self.tile_modifier_system.ProcessTileModifiers(self.world)



                # Action related
                inputs = self.GetInputs()
                self.controller_input_system.HandleInputEventDriven(self.joystick, inputs, self.world)
                self.ai_system.ProcessAI(self.world)
                self.actions_processing_system.ProcessActions(self.world, self.game_timer.dt)





                # Entity creation related
                self.factory_system.ProcessOrders(self.world)




                # Movement related
                self.gravity_system.ProcessGravity(self.world)
                self.friction_system.ProcessFriction(self.world)
                self.kinematics_system.UpdateKinematics(self.world, self.game_timer.dt)
                self.tilemap_collision_system.ProcessTilemapCollisions(self.world)
                self.kinematics_system.ValidatePosition(self.world)


                self.status_processing_system.ProcessStatus(self.world)





                # Clean up entities
                self.world.entity_manager.RegisterNewEntities()
                self.world.entity_manager.CleanUpDeadEntities()





            # Render and sound
            if self.render_timer.Update():
                self.sprite_animation_system.UpdateEntitySprites(self.world, self.render_timer.dt)
                self.render_system.RenderAll(self.world, self.render_timer.dt)
                self.sound_system.PlaySounds(self.world, self.render_timer.dt)



        self.Quit()

        return 0
