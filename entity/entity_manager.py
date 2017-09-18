# Standard library
import sys
import ctypes

sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/entity')
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/component')
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/system')



# Game
import entity
import display_component
import position_component
import velocity_component
import gravity_component
import acceleration_component
import shape_component
import actions_component
import controller_input_component
import ai_component
import following_ai_component
import tilemap_collidable_component
import orientation_component
import running_action_component
import panning_action_component
import jumping_action_component
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

        # Position
        hero.position = position_component.PositionComponent()
        hero.position.x = 160
        hero.position.y = 240
        hero.position.x_proposed = hero.position.x
        hero.position.y_proposed = hero.position.y

        # Velocity
        hero.velocity = velocity_component.VelocityComponent()

        # Running action
        hero.running_action = running_action_component.RunningActionComponent()
        hero.running_action.speed = 128

        # Jumping action
        hero.jumping_action = jumping_action_component.JumpingActionComponent()
        hero.jumping_action.speed = 512.

        # Shooting action
        hero.shooting_action = shooting_action_component.ShootingActionComponent()
        hero.shooting_action.max_bullets = 3
        hero.shooting_action.cooldown = 2
        hero.shooting_action.bullet = 'BusterShot'
        hero.shooting_action.last_shot = 0

        # Gravity
        hero.gravity = gravity_component.GravityComponent()
        hero.gravity.g = 64
        hero.gravity.terminal_velocity = 512.

        # Acceleration
        hero.acceleration = acceleration_component.AccelerationComponent()

        # Shape
        hero.shape = shape_component.ShapeComponent()
        hero.shape.w = 16
        hero.shape.h = 32

        # Actions component
        hero.actions = actions_component.ActionsComponent()

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

        # Position
        buster_shot.position = position_component.PositionComponent()

        # Velocity
        buster_shot.velocity = velocity_component.VelocityComponent()

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
        camera.position = position_component.PositionComponent()
        camera.position.x = self.entitys['hero'].position.x
        camera.position.y = self.entitys['hero'].position.y
        camera.position.x_proposed = camera.position.x
        camera.position.y_proposed = camera.position.y

        # Velocity
        camera.velocity = velocity_component.VelocityComponent()
        camera.velocity.vx = 0
        camera.velocity.vy = 0

        # Panning
        camera.panning_action = panning_action_component.PanningActionComponent()
        camera.panning_action.xspeed = 256.
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
