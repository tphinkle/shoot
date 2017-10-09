# Standard library
import sys
import ctypes

# SDL
import sdl2
import sdl2.sdlimage
import sdl2.sdlttf

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
import sprite_animation_system

import tile_modifier_system

import controller_input_system
import ai_system
import actions_processing_system

import friction_system
import kinematics_system
import gravity_system


import status_processing_system



import tilemap_collision_system



class System:
    def __init__(self):

        self.InitializeSDL()
        self.InitializeTimers()
        self.InitializeSubsystems()
        self.InitializeWorld()


    def InitializeSDL(self):
        # SDL sub systems

        # TTF
        sdl2.sdlttf.TTF_Init()

        # Video
        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)

        # Window
        self.window = sdl2.SDL_CreateWindow("Shoot",\
            sdl2.SDL_WINDOWPOS_UNDEFINED,\
            sdl2.SDL_WINDOWPOS_UNDEFINED,
            640,\
            480,\
            sdl2.SDL_WINDOW_SHOWN)

        # renderer
        self.sdl_renderer = sdl2.SDL_CreateRenderer(self.window, -1,\
            sdl2.SDL_RENDERER_ACCELERATED)
        sdl2.SDL_SetRenderDrawColor(self.sdl_renderer, 255, 255, 255, 0)

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
        self.render_system = render_system.RenderSystem(self.sdl_renderer, self.window)
        self.sprite_animation_system = sprite_animation_system.SpriteAnimationSystem()


        # Actions systems
        self.controller_input_system = controller_input_system.ControllerInputSystem(self.joystick)
        self.actions_processing_system = actions_processing_system.ActionsProcessingSystem()



        self.tile_modifier_system = tile_modifier_system.TileModifierSystem()

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


    def Run(self):
        # Begin main loop
        self.LoadGame()
        self.running = True
        while self.running:

            # Game
            if self.game_timer.Update():

                print 'new game loop update'


                inputs = self.GetInputs()
                self.controller_input_system.HandleInputEventDriven(self.joystick, inputs, self.world)
                self.ai_system.ProcessAI(self.world)



                self.tile_modifier_system.ProcessTileModifiers(self.world)

                self.actions_processing_system.ProcessActions(self.world, self.game_timer.dt)



                self.gravity_system.ProcessGravity(self.world)



                self.friction_system.ProcessFriction(self.world)

                self.kinematics_system.UpdateKinematics(self.world, self.game_timer.dt)



                self.tilemap_collision_system.ProcessTilemapCollisions(self.world)


                self.kinematics_system.ValidatePosition(self.world)


                self.status_processing_system.ProcessStatusEffects(self.world)




            # Render
            if self.render_timer.Update():
                self.sprite_animation_system.UpdateEntitySprites(self.world, self.render_timer.dt)
                self.render_system.RenderAll(self.world)



        return 0
