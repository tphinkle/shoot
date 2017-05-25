# Standard library
import sys
import ctypes

# SDL
import sdl2
import sdl2.sdlimage

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
import controller_input_system
import actions_process_system
import movement_process_system
import gravity_system
import acceleration_system
import ai_system
import tilemap_collision_system



class System:
    def __init__(self):
        self.InitializeSDL()
        self.InitializeTimers()
        self.InitializeSubsystems()
        self.InitializeWorld()


    def InitializeSDL(self):
        # SDL sub systems

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
        self.controller_input_system = controller_input_system.ControllerInputSystem()
        self.actions_process_system = actions_process_system.ActionsProcessSystem()
        self.movement_process_system = movement_process_system.MovementProcessSystem()
        self.gravity_system = gravity_system.GravitySystem()
        self.acceleration_system = acceleration_system.AccelerationSystem()
        self.ai_system = ai_system.AISystem()
        self.tilemap_collision_system = tilemap_collision_system.TilemapCollisionSystem()

    def InitializeWorld(self):
        self.world = world.World()
        # Entities

    def LoadGame(self):
        self.world.LoadGame()




    def Run(self):
        # Begin main loop
        self.LoadGame()
        running = True
        while running:


            # Poll events
            inputs = []
            while sdl2.SDL_PollEvent(ctypes.byref(self.input)) != 0:
                if self.input.type == sdl2.SDL_QUIT:
                    running = False
                    break

                else:
                    pass

            # Game
            if self.game_timer.Update():
                self.controller_input_system.HandleInputJoystickStateDriven(self.joystick, self.world)

                self.actions_process_system.ProcessActions(self.world)
                self.gravity_system.ProcessGravity(self.world)
                self.acceleration_system.ProcessAcceleration(self.world, self.game_timer.dt)
                self.movement_process_system.ProcessMovement(self.world, self.game_timer.dt)
                self.ai_system.ProcessAI(self.world)
                self.tilemap_collision_system.ProcessTilemapCollisions(self.world)
                #self.gravity_system.CheckGrounded(self.world)
                self.movement_process_system.ValidateMovement(self.world)


            # Render
            if self.render_timer.Update():
                self.render_system.RenderAll(self.world)



        return 0
