# Standard library
import sys
import ctypes

sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/entity')
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/component')
sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/system')



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
import following_component
import tilemap_collidable_component
import orientation_component


# SDL
import sdl2

class EntityManager():
    def __init__(self):
        self.entitys = {}
        pass

    def CreateHero(self):
        hero = self.CreateEntity('hero')

        # Display
        hero.display = display_component.DisplayComponent(b'/home/prestonh/Desktop/Programming/gamedev/shoot/resources/X.png')
        hero.display.source_rect = sdl2.SDL_Rect(213,18,30,34)
        hero.display.z = 1

        # Position
        hero.position = position_component.PositionComponent()
        hero.position.x = 100
        hero.position.y = 100

        # Velocity
        hero.velocity = velocity_component.VelocityComponent()
        hero.velocity.xspeed = 48.


        # Gravity
        hero.gravity = gravity_component.GravityComponent()

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

        # orientation
        hero.orientation = orientation_component.OrientationComponent()

        return hero



    def CreateCamera(self):
        camera = self.CreateEntity('camera')

        # Position
        camera.position = position_component.PositionComponent()
        camera.position.x = 0
        camera.position.y = 0

        # Velocity
        camera.velocity = velocity_component.VelocityComponent()
        camera.velocity.vx = 0
        camera.velocity.vy = 0
        camera.velocity.xspeed = 256.
        camera.velocity.yspeed = 256.

        # Shape
        camera.shape = shape_component.ShapeComponent()
        camera.shape.w = 320
        camera.shape.h = 240

        # Actions
        camera.actions = actions_component.ActionsComponent()



        # AI
        camera.ai = ai_component.AIComponent()
        camera.ai.behavior = 'following'

        # Following
        camera.following = following_component.FollowingComponent(self.entitys['hero'])
        camera.following.xlag = camera.shape.w/4.
        camera.following.ylag = camera.shape.h/4.

        return camera

    def CreateEntity(self, key):
        new_entity = entity.Entity(key)
        self.entitys[key] = new_entity

        return new_entity

    def DeleteEntity(self, key):
        pass
