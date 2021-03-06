# Standard library
import sys
import ctypes
import random

sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/entity')
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/component')
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/system')



# Game
import entity
import display_component
import gravity_component


import kinematics_component

import shape_component
import active_component
import controller_input_component
import ai_component
import following_ai_component
import tilemap_collidable_component
import orientation_component


import jump_action_component
import dash_action_component
import shoot_action_component
import move_action_component

import status_component
import factory_component
import sprite_animation_component
import friction_component
import sound_component

import on_clear_component


# SDL
import sdl2

'''
Notes:

    - Look up 'Builder' design pattern, which can set up component-based entity
one component at a time, based on data

    -

    -

    -


'''



class EntityManager():
    def __init__(self):
        self.new_entities = []
        self.remove_entities = []
        self.entities = {}
        self.entity_counts = {}

        self.entity_creation_routines = {}
        self.entity_creation_routines['hero'] = self.CreateHero
        self.entity_creation_routines['camera'] = self.CreateCamera
        self.entity_creation_routines['buster_shot'] = self.CreateBusterShot
        self.entity_creation_routines['charge_buster_shot_lite'] = self.CreateChargeBusterShotLite
        self.entity_creation_routines['charge_buster_shot_medium'] = self.CreateChargeBusterShotMedium
        self.entity_creation_routines['charge_buster_shot_heavy'] = self.CreateChargeBusterShotHeavy


        pass


    def CreateHero(self):

        type = 'hero'
        hero = entity.Entity(type)

        # Display
        hero.display = display_component.DisplayComponent(b'/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/X.png')
        hero.display.source_rect = sdl2.SDL_Rect(213,18,30,34)
        hero.display.z = 1

        # Friction
        hero.friction = friction_component.FrictionComponent()
        hero.friction.acceleration = 1750.

        # Kinematics
        hero.kinematics = kinematics_component.KinematicsComponent()
        hero.kinematics.x = 800
        hero.kinematics.y = 800
        hero.kinematics.x_proposed = hero.kinematics.x
        hero.kinematics.y_proposed = hero.kinematics.y



        # Actions component
        hero.active = active_component.ActiveComponent()

        # Running action
        hero.move_action = move_action_component.NormalMoveActionComponent()
        hero.move_action.movement_type = 'normal'
        hero.move_action.direction = 'right'
        hero.move_action.runn_base_speed = 128
        hero.move_action.float_base_speed = 128
        hero.active.actions.append(hero.move_action)

        # Jumping action
        hero.jump_action = jump_action_component.JumpActionComponent()
        hero.jump_action.period = .25
        hero.jump_action.initial_speed = 300.
        hero.jump_action.acceleration = 640.
        hero.active.actions.append(hero.jump_action)

        # Air jumping action
        hero.airjump_action = jump_action_component.AirJumpActionComponent()
        hero.airjump_action.period = .25
        hero.airjump_action.initial_speed = 300.
        hero.airjump_action.acceleration = 640.
        hero.active.actions.append(hero.airjump_action)

        # Dashing action
        hero.dash_action = dash_action_component.DashActionComponent()
        hero.dash_action.period = 0.5
        hero.dash_action.base_speed = 256
        hero.active.actions.append(hero.dash_action)

        # Buster gun
        buster = shoot_action_component.NormalGun()
        buster.name = 'buster'
        buster.max_bullets_out = 3
        buster.owner = hero
        buster.cooldown_timer = 1
        buster.bullet_name = 'buster_shot'
        buster.x_offset = 22
        buster.y_offset = 16



        # Shooting action
        hero.shoot_buster_action = shoot_action_component.ShootActionComponent()
        hero.shoot_buster_action.gun = buster
        hero.active.actions.append(hero.shoot_buster_action)


        '''
        # Charge buster gun
        charge_buster = shoot_action_component.ChargeGun()
        charge_buster.name = 'charge_buster'
        charge_buster.max_bullets_out = 3
        charge_buster.owner = hero
        charge_buster.cooldown = 0.5
        charge_buster.charge_times = [0.5, 1, 1.5]
        charge_buster.bullet_names = ['charge_buster_shot_lite', 'charge_buster_shot_medium', 'charge_buster_shot_heavy']
        charge_buster.x_offset = 22
        charge_buster.y_offset = 16
        hero.shoot_action.AttachGun(charge_buster)
        '''

        # Controller input component
        hero.controller_input = controller_input_component.ControllerInputComponent()

        hero.controller_input.command_mapping['Left_Press'] = [{'action': hero.move_action, 'trigger':'start', 'direction':'left'}]
        hero.controller_input.command_mapping['Right_Press'] = [{'action': hero.move_action, 'trigger':'start', 'direction':'right'}]

        hero.controller_input.command_mapping['LeftRight_Release'] = [{'action':hero.move_action, 'trigger':'stop'}]


        # Shooting class
        # Needs class, action, gun, and trigger
        hero.controller_input.command_mapping['Y_Press'] = [{'action':hero.shoot_buster_action, 'trigger':'start'}]
        hero.controller_input.command_mapping['Y_Release'] = [{'action':hero.shoot_buster_action, 'trigger':'stop'}]




        # Dashing class
        # Need class, trigger
        hero.controller_input.command_mapping['A_Press'] = [{'action':hero.dash_action, 'trigger': 'start'}]
        hero.controller_input.command_mapping['A_Release'] = [{'action':hero.dash_action, 'trigger': 'stop'}]




        # Jumping class
        # Needs trigger, start, stop
        hero.controller_input.command_mapping['B_Press'] = [{'action': hero.jump_action,  'trigger':'start'},
        {'action': hero.airjump_action, 'trigger':'start'}]
        hero.controller_input.command_mapping['B_Release'] = [{'action': hero.jump_action, 'trigger':'stop'},
        {'action': hero.airjump_action, 'trigger':'stop'}]



        # Gravity
        hero.gravity = gravity_component.GravityComponent()
        hero.gravity.g = 1600.
        hero.gravity.terminal_velocity = 1500.



        # Shape
        hero.shape = shape_component.ShapeComponent()
        hero.shape.w = 16
        hero.shape.h = 32





        # Tilemap collidable component
        hero.tilemap_collidable = tilemap_collidable_component.TilemapCollidableComponent()
        hero.tilemap_collidable.death_on_collision = False

        # Orientation
        hero.orientation = orientation_component.OrientationComponent()


        # Status
        hero.status = status_component.StatusComponent()
        hero.status.immunities = []

        # Factory component
        hero.factory = factory_component.FactoryComponent()
        hero.factory.orders = []


        # Sprite animations
        hero.sprite_animation = sprite_animation_component.SpriteAnimationComponent()


        run_animation = sprite_animation_component.Animation('run')
        run_animation.rects = [sdl2.SDL_Rect(319, 19, 30, 34),
		sdl2.SDL_Rect(350, 19, 20, 34),
		sdl2.SDL_Rect(371, 18, 23, 35),
		sdl2.SDL_Rect(394, 19, 32, 34),
		sdl2.SDL_Rect(426, 20, 34, 33),
		sdl2.SDL_Rect(460, 20, 26, 33),
		sdl2.SDL_Rect(489, 19, 22, 34),
		sdl2.SDL_Rect(511, 18, 25, 35),
		sdl2.SDL_Rect(538, 19, 31, 34),
		sdl2.SDL_Rect(570, 20, 34, 33),
		sdl2.SDL_Rect(604, 20, 29, 33)]
        run_animation.clock = 0.
        run_animation.period = .05
        run_animation.total_frames = len(run_animation.rects)
        run_animation.type = 'cyclical'
        hero.sprite_animation.animations.append(run_animation)

        shoot_animation = sprite_animation_component.Animation('shoot')
        shoot_animation.rects = [sdl2.SDL_Rect(6, 167, 30, 34),
        sdl2.SDL_Rect(41, 167, 29, 33)]

        shoot_animation.clock = 0.
        shoot_animation.period = .05
        shoot_animation.total_frames = len(shoot_animation.rects)
        shoot_animation.type = 'terminating'
        hero.sprite_animation.animations.append(shoot_animation)


        runshoot_animation = sprite_animation_component.Animation('runshoot')
        runshoot_animation.rects = [sdl2.SDL_Rect(290, 71, 29, 34),
		sdl2.SDL_Rect(319, 70, 32, 35),
		sdl2.SDL_Rect(351, 71, 35, 34),
		sdl2.SDL_Rect(387, 72, 38, 33),
		sdl2.SDL_Rect(426, 72, 34, 33),
		sdl2.SDL_Rect(460, 71, 31, 34),
		sdl2.SDL_Rect(491, 70, 33, 35),
		sdl2.SDL_Rect(524, 71, 35, 34),
		sdl2.SDL_Rect(560, 72, 37, 33),
		sdl2.SDL_Rect(597, 72, 35, 33)]
        runshoot_animation.clock = 0.
        runshoot_animation.period = .05
        runshoot_animation.total_frames = len(runshoot_animation.rects)
        runshoot_animation.type = 'cyclical'
        hero.sprite_animation.animations.append(runshoot_animation)


        float_animation = sprite_animation_component.Animation('float')
        float_animation.rects = [sdl2.SDL_Rect(5, 73, 24, 37),
		sdl2.SDL_Rect(34, 69, 15, 41),
		sdl2.SDL_Rect(55, 64, 19, 46),
		sdl2.SDL_Rect(77, 69, 23, 41),
		sdl2.SDL_Rect(102, 68, 27, 42),
		sdl2.SDL_Rect(134, 72, 24, 38),
		sdl2.SDL_Rect(159, 78, 30, 32)]
        float_animation.clock = 0.
        float_animation.period = .05
        float_animation.total_frames = len(float_animation.rects)
        hero.sprite_animation.animations.append(float_animation)


        dash_animation = sprite_animation_component.Animation('dash')
        dash_animation.rects = [sdl2.SDL_Rect(287, 127, 28, 31),
        sdl2.SDL_Rect(319, 132, 38, 26)]
        dash_animation.clock = 0.
        dash_animation.period = .05
        dash_animation.total_frames = len(dash_animation.rects)
        dash_animation.type = 'terminating'
        hero.sprite_animation.animations.append(dash_animation)

        jump_animation = sprite_animation_component.Animation('jump')
        jump_animation.rects = [sdl2.SDL_Rect(5, 73, 24, 37),
		sdl2.SDL_Rect(34, 69, 15, 41),
		sdl2.SDL_Rect(55, 64, 19, 46)]
        jump_animation.clock = 0.
        jump_animation.period = .15
        jump_animation.total_frames = len(jump_animation.rects)
        jump_animation.type = 'terminating'
        hero.sprite_animation.animations.append(jump_animation)

        float_animation = sprite_animation_component.Animation('float')
        float_animation.rects = [sdl2.SDL_Rect(77, 69, 23, 41)]
        float_animation.clock = 0.
        float_animation.period = .25
        float_animation.total_frames = len(float_animation.rects)
        float_animation.type = 'terminating'
        hero.sprite_animation.animations.append(float_animation)


        default_animation = sprite_animation_component.Animation('default')

        default_animation.rects = [sdl2.SDL_Rect(213, 18, 30, 34),
        sdl2.SDL_Rect(247, 18, 30, 34),
        sdl2.SDL_Rect(281, 18, 30, 34)]
        default_animation.clock = 0.
        default_animation.period = 1
        default_animation.total_frames = len(default_animation.rects)
        default_animation.type = 'cyclical'
        hero.sprite_animation.animations.append(default_animation)


        hero.sprite_animation.default_animation = default_animation
        hero.sprite_animation.active_animation = default_animation

        return hero


    def CreateCamera(self):

        # Create
        type = 'camera'
        camera = entity.Entity(type)

        # Position
        camera.kinematics = kinematics_component.KinematicsComponent()
        camera.kinematics.x = self.entities['hero_0'].kinematics.x
        camera.kinematics.y = self.entities['hero_0'].kinematics.y

        camera.kinematics.x_proposed = camera.kinematics.x
        camera.kinematics.y_proposed = camera.kinematics.y


        # Actions
        camera.active = active_component.ActiveComponent()


        # Panning
        camera.free_move_action = move_action_component.FreeMoveActionComponent()
        camera.free_move_action.xspeed = 128.
        camera.free_move_action.yspeed = 640.
        camera.free_move_action.period = 0
        camera.active.actions.append(camera.free_move_action)

        # Shape
        camera.shape = shape_component.ShapeComponent()
        camera.shape.w = 320
        camera.shape.h = 240


        # AI
        camera.ai = ai_component.AIComponent()
        camera.ai.behaviors.append('following')

        # Following
        camera.following_ai = following_ai_component.FollowingAIComponent(self.entities['hero_0'])
        camera.following_ai.xlag = camera.shape.w/3.
        camera.following_ai.ylag = camera.shape.h/3.


        return camera



    def CreateBusterShot(self):


        # Create
        type = 'buster_shot'
        buster_shot = entity.Entity(type)

        # Display
        buster_shot.display = display_component.DisplayComponent(b'/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/X.png')
        buster_shot.display.source_rect = sdl2.SDL_Rect(5, 377, 8, 6)
        buster_shot.display.z = 1

        # Shape
        buster_shot.shape = shape_component.ShapeComponent()
        buster_shot.shape.w = 8
        buster_shot.shape.h = 6

        # Kinematics
        buster_shot.kinematics = kinematics_component.KinematicsComponent()
        buster_shot.kinematics.vy = 0

        # Orientation
        buster_shot.orientation = orientation_component.OrientationComponent()

        # Tilemap collidable component
        buster_shot.tilemap_collidable = tilemap_collidable_component.TilemapCollidableComponent()
        buster_shot.tilemap_collidable.death_on_collision = True

        # Status
        buster_shot.status = status_component.StatusComponent()
        buster_shot.status.hp = 1
        buster_shot.status.dead = False

        # On clear
        buster_shot.on_clear = on_clear_component.OnClearComponent()


        return buster_shot

    def CreateChargeBusterShotLite(self):


        # Create
        type = 'charge_buster_shot_lite'
        buster_shot = entity.Entity(type)

        # Display
        buster_shot.display = display_component.DisplayComponent(b'/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/X.png')
        buster_shot.display.source_rect = sdl2.SDL_Rect(163, 374, 38, 12)
        buster_shot.display.z = 1

        # Shape
        buster_shot.shape = shape_component.ShapeComponent()
        buster_shot.shape.w = 8
        buster_shot.shape.h = 6

        # Kinematics
        buster_shot.kinematics = kinematics_component.KinematicsComponent()
        buster_shot.kinematics.vy = 0

        # Orientation
        buster_shot.orientation = orientation_component.OrientationComponent()

        # Tilemap collidable component
        buster_shot.tilemap_collidable = tilemap_collidable_component.TilemapCollidableComponent()
        buster_shot.tilemap_collidable.death_on_collision = True

        # Status
        buster_shot.status = status_component.StatusComponent()
        buster_shot.status.hp = 1
        buster_shot.status.dead = False

        # On clear
        buster_shot.on_clear = on_clear_component.OnClearComponent()


        return buster_shot

    def CreateChargeBusterShotMedium(self):


        # Create
        type = 'charge_buster_shot_medium'
        buster_shot = entity.Entity(type)

        # Display
        buster_shot.display = display_component.DisplayComponent(b'/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/X.png')
        buster_shot.display.source_rect = sdl2.SDL_Rect(62, 407, 27, 24)
        buster_shot.display.z = 1

        # Shape
        buster_shot.shape = shape_component.ShapeComponent()
        buster_shot.shape.w = 8
        buster_shot.shape.h = 6

        # Kinematics
        buster_shot.kinematics = kinematics_component.KinematicsComponent()
        buster_shot.kinematics.vy = 0

        # Orientation
        buster_shot.orientation = orientation_component.OrientationComponent()

        # Tilemap collidable component
        buster_shot.tilemap_collidable = tilemap_collidable_component.TilemapCollidableComponent()
        buster_shot.tilemap_collidable.death_on_collision = True

        # Status
        buster_shot.status = status_component.StatusComponent()
        buster_shot.status.hp = 1
        buster_shot.status.dead = False

        # On clear
        buster_shot.on_clear = on_clear_component.OnClearComponent()


        return buster_shot

    def CreateChargeBusterShotHeavy(self):


        # Create
        type = 'charge_buster_shot_heavy'
        buster_shot = entity.Entity(type)

        # Display
        buster_shot.display = display_component.DisplayComponent(b'/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/X.png')
        buster_shot.display.source_rect = sdl2.SDL_Rect(35, 496, 46, 31)
        buster_shot.display.z = 1

        # Shape
        buster_shot.shape = shape_component.ShapeComponent()
        buster_shot.shape.w = 8
        buster_shot.shape.h = 6

        # Kinematics
        buster_shot.kinematics = kinematics_component.KinematicsComponent()
        buster_shot.kinematics.vy = 0

        # Orientation
        buster_shot.orientation = orientation_component.OrientationComponent()

        # Tilemap collidable component
        buster_shot.tilemap_collidable = tilemap_collidable_component.TilemapCollidableComponent()
        buster_shot.tilemap_collidable.death_on_collision = True

        # Status
        buster_shot.status = status_component.StatusComponent()
        buster_shot.status.hp = 1
        buster_shot.status.dead = False

        # On clear
        buster_shot.on_clear = on_clear_component.OnClearComponent()


        return buster_shot


    def CreateEntity(self, entity_name, creation_time = 'end_of_update'):
        '''
        creation_time arg is a hack that was put together; hte error was cuased when
        a new entity was added in the middle of iterating over the entities dict in some subsystem
        e.g. when creating a bullet, new bullet is added
        we defer creation of new entity until end of loop
        but, this is a problem with camera which must be immediately attached to an entity on creation;
        this is a hack to fix that issue
        we should have better creation routines for the camera
        '''

        print entity_name

        entity = self.entity_creation_routines[entity_name]()

        if creation_time == 'end_of_update':
            self.QueueNewEntity(entity)

        elif creation_time == 'instant':
            self.RegisterEntity(entity)

        return entity

    '''
    Creation routines
    '''

    def QueueNewEntity(self, entity):
        self.new_entities.append(entity)

    def RegisterNewEntities(self):
        for new_entity in self.new_entities:
            self.RegisterEntity(new_entity)

        self.new_entities = []


    def RegisterEntity(self, new_entity):

        type = new_entity.type
        id = self.GenerateID(type)
        key = type + '_' + id

        new_entity.id = id
        new_entity.key = key


        self.entities[key] = new_entity

    def GenerateID(self, entity_type):
        if entity_type not in self.entity_counts.keys():
            self.entity_counts[entity_type] = 0

        elif entity_type in self.entity_counts.keys():
            self.entity_counts[entity_type] += 1

        id = str(self.entity_counts[entity_type])

        return id




    '''
    Destruction routines
    '''


    # Clean this code up
    # It works for entities that die from lack of HP
    # It needs to be extended for cleaning up entities that need to be removed
    # for other reasons, e.g. moving to a new room should clean up some entities
    # Right now this code needs to be modified when we add in that type of clean up
    # routine

    def CleanUpDeadEntities(self):
        for key, entity in self.entities.iteritems():
            if entity.status:
                if entity.status.hp == -1:
                    self.remove_entities.append(entity)

        for entity in self.remove_entities:
            self.RemoveEntity(entity)

        self.remove_entities = []



    def RemoveEntity(self, entity):
        # Call entity's clean up functions
        if entity.on_clear:
            for function in entity.on_clear.functions:
                function()



        remove_entity = self.entities.pop(entity.key)
        del remove_entity
