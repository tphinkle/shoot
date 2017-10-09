# Standard library
import sys
import ctypes

sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/entity')
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/component')
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/system')



# Game
import entity
import display_component
import gravity_component


import kinematics_component

import shape_component
import actions_component
import controller_input_component
import ai_component
import following_ai_component
import tilemap_collidable_component
import orientation_component
import running_floating_action_component
import panning_action_component
import jumping_action_component
import dashing_action_component
import shooting_action_component
import status_component
import factory_component
import sprite_animation_component
import friction_component
import sound_component


# SDL
import sdl2

class EntityManager():
    def __init__(self):
        self.entitys = {}
        pass

    def CreateHero(self):
        hero = self.CreateEntity('hero')

        # Display
        hero.display = display_component.DisplayComponent(b'/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/X.png')
        hero.display.source_rect = sdl2.SDL_Rect(213,18,30,34)
        hero.display.z = 1

        # Friction
        hero.friction = friction_component.FrictionComponent()
        hero.friction.acceleration = 1000.

        # Kinematics
        hero.kinematics = kinematics_component.KinematicsComponent()
        hero.kinematics.x = 800
        hero.kinematics.y = 800
        hero.kinematics.x_proposed = hero.kinematics.x
        hero.kinematics.y_proposed = hero.kinematics.y





        # Actions component
        hero.actions = actions_component.ActionsComponent()

        # Running action
        hero.running_floating_action = running_floating_action_component.RunningFloatingActionComponent()
        hero.running_floating_action.direction = 'right'
        hero.running_floating_action.running_base_speed = 128
        hero.running_floating_action.floating_base_speed = 128

        # Jumping action
        hero.jumping_action = jumping_action_component.JumpingActionComponent()
        hero.jumping_action.period = .25
        hero.jumping_action.initial_speed = 300.
        hero.jumping_action.acceleration = 640.

        # Dashing action
        hero.dashing_action = dashing_action_component.DashingActionComponent()
        hero.dashing_action.period = 0.5
        hero.dashing_action.base_speed = 256



        # Shooting action
        hero.shooting_action = shooting_action_component.ShootingActionComponent()
        hero.shooting_action.max_bullets = 3
        hero.shooting_action.cooldown = 2
        hero.shooting_action.bullet = 'BusterShot'
        hero.shooting_action.last_shot = 0

        # Gravity
        hero.gravity = gravity_component.GravityComponent()
        hero.gravity.g = 1600.
        hero.gravity.terminal_velocity = 1500.



        # Shape
        hero.shape = shape_component.ShapeComponent()
        hero.shape.w = 16
        hero.shape.h = 32



        # Controller input component
        hero.controller_input = controller_input_component.ControllerInputComponent()

        # Tilemap collidable component
        hero.tilemap_collidable = tilemap_collidable_component.TilemapCollidableComponent()

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


        running_animation = sprite_animation_component.Animation('running')
        running_animation.rects = [sdl2.SDL_Rect(319, 19, 30, 34),
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
        running_animation.clock = 0.
        running_animation.period = .05
        running_animation.total_frames = len(running_animation.rects)
        running_animation.type = 'cyclical'
        hero.sprite_animation.animations.append(running_animation)


        floating_animation = sprite_animation_component.Animation('floating')
        floating_animation.rects = [sdl2.SDL_Rect(5, 73, 24, 37),
		sdl2.SDL_Rect(34, 69, 15, 41),
		sdl2.SDL_Rect(55, 64, 19, 46),
		sdl2.SDL_Rect(77, 69, 23, 41),
		sdl2.SDL_Rect(102, 68, 27, 42),
		sdl2.SDL_Rect(134, 72, 24, 38),
		sdl2.SDL_Rect(159, 78, 30, 32)]
        floating_animation.clock = 0.
        floating_animation.period = .05
        floating_animation.total_frames = len(floating_animation.rects)
        hero.sprite_animation.animations.append(floating_animation)


        dashing_animation = sprite_animation_component.Animation('dashing')
        dashing_animation.rects = [sdl2.SDL_Rect(287, 127, 28, 31),
        sdl2.SDL_Rect(319, 132, 38, 26)]
        dashing_animation.clock = 0.
        dashing_animation.period = .05
        dashing_animation.total_frames = len(dashing_animation.rects)
        dashing_animation.type = 'terminating'
        hero.sprite_animation.animations.append(dashing_animation)


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



    def CreateCamera(self):
        camera = self.CreateEntity('camera')

        # Position
        camera.kinematics = kinematics_component.KinematicsComponent()
        camera.kinematics.x = self.entitys['hero'].kinematics.x
        camera.kinematics.y = self.entitys['hero'].kinematics.y

        camera.kinematics.x_proposed = camera.kinematics.x
        camera.kinematics.y_proposed = camera.kinematics.y


        # Panning
        camera.panning_action = panning_action_component.PanningActionComponent()
        camera.panning_action.xspeed = 128.
        camera.panning_action.yspeed = 640.
        camera.panning_action.period = 0

        # Shape
        camera.shape = shape_component.ShapeComponent()
        camera.shape.w = 320
        camera.shape.h = 240

        # Actions
        camera.actions = actions_component.ActionsComponent()

        # AI
        camera.ai = ai_component.AIComponent()
        camera.ai.behaviors.append('following')

        # Following
        camera.following_ai = following_ai_component.FollowingAIComponent(self.entitys['hero'])
        camera.following_ai.xlag = camera.shape.w/3.
        camera.following_ai.ylag = camera.shape.h/3.


        return camera

    def CreateEntity(self, key, specifications = None):
        new_entity = entity.Entity(key)
        self.entitys[key] = new_entity

        return new_entity



    def DeleteEntity(self, key):
        pass
