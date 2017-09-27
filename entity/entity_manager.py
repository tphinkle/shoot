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
        hero.running_floating_action.running_base_speed = 128
        hero.running_floating_action.floating_base_speed = 128

        # Jumping action
        hero.jumping_action = jumping_action_component.JumpingActionComponent()
        hero.jumping_action.base_speed = 1024.

        # Dashing action
        hero.dashing_action = dashing_action_component.DashingActionComponent()
        hero.dashing_action.base_speed = 256



        # Shooting action
        hero.shooting_action = shooting_action_component.ShootingActionComponent()
        hero.shooting_action.max_bullets = 3
        hero.shooting_action.cooldown = 2
        hero.shooting_action.bullet = 'BusterShot'
        hero.shooting_action.last_shot = 0

        # Gravity
        hero.gravity = gravity_component.GravityComponent()
        hero.gravity.g = 64.
        hero.gravity.terminal_velocity = 512.


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

        '''
        First-class function that returns the hero's position; this is the
        spawn location for the factory.
        '''
        def spawn_location():
            return hero.position.x, hero.position.y
        hero.factory.spawn_location = spawn_location


        return hero



    def CreateBusterShot(self, customer = None):
        buster_shot = self.CreateEntity('BusterShot')

        # Kinematics
        buster_shot.kinematics = kinematics_component.KinematicsComponent()


        # Shape
        buster_shot.shape = shape_component.ShapeComponent()
        buster_shot.shape.w = 16
        buster_shot.shape.h = 16

        # Damage component
        # buster_shot.damage = damage_component.DamageComponent()
        # buster_shot.damage.damage = 3

        return buster_shot



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
