# Python standard library
import sys

# Game specific
sys.path.append('../component/')
import factory_component

class ShootingActionProcessingSystem(object):



    def __init__(self):
        pass

    def Trigger(self, entity, action):

        # Get gun name
        gun_name = action['gun']

        # Get specific gun
        gun = entity.shooting_action.guns[gun_name]

        # Get gun type
        gun_type = gun.type

        # Divert to correct processing type
        if gun_type == 'normal':
            self.TriggerNormalShot(entity, gun, action)

        elif gun_type == 'charge':
            self.TriggerChargeShot(entity, gun, action)


    def TriggerNormalShot(self, entity, gun, action):
        # Start
        if action['trigger'] == 'start':


            # Check cooldown
            if gun.cooldown_timer >= gun.cooldown and gun.bullets_out < gun.max_bullets_out:

                # Fire gun
                self.FireGun(entity, gun)

                # Reset timer
                gun.cooldown_timer = 0


        # Stop
        elif action['trigger'] == 'stop':
            pass


    def TriggerChargeShot(self, entity, gun, action):
        # Start
        if action['trigger'] == 'start':
            gun.status = 'active'


        # Stop
        elif action['trigger'] == 'stop':

            gun.bullet_name = gun.bullet_names[0]

            # Fire gun
            self.FireGun(entity, gun)

            # Update status
            gun.status = 'inactive'



    def FireGun(self, entity, gun):
        bullet_name = gun.bullet_name


        def on_creation(new_bullet):


            # Set orientation
            new_bullet.orientation.xorientation = entity.orientation.xorientation


            # Set x
            if new_bullet.orientation.xorientation == 'right':
                new_bullet.kinematics.x = entity.kinematics.x + gun.x_offset


            elif new_bullet.orientation.xorientation == 'left':

                new_bullet.kinematics.x = entity.kinematics.x + entity.shape.w - gun.x_offset - new_bullet.shape.w

            new_bullet.kinematics.x_proposed = new_bullet.kinematics.x

            # Set y
            new_bullet.kinematics.y = entity.kinematics.y + gun.y_offset
            new_bullet.kinematics.y_proposed = new_bullet.kinematics.y


            # Set direction and velocity
            new_bullet.kinematics.vx = 256
            if new_bullet.orientation.xorientation == 'left':
                new_bullet.kinematics.vx *= -1

            new_bullet.kinematics.vy = 0

            # Increase max bullets
            gun.bullets_out += 1



        # Create order and send to factory
        order = factory_component.Order(bullet_name, on_creation)
        entity.factory.orders.append(order)




    def ProcessAction(self, world, dt):
        for key, entity in world.entity_manager.entities.iteritems():
            if entity.shooting_action != None:
                for name, gun in entity.shooting_action.guns.iteritems():

                    if gun.type == 'normal':
                        self.ProcessNormalGun(entity, gun, dt)

                    elif gun.type == 'charge':
                        self.ProcessChargeGun(entity, gun, dt)



    def ProcessNormalGun(self, entity, gun, dt):
        # Active
        if gun.status == 'active':
            pass

        # Inactive
        elif gun.status == 'inactive':
            gun.cooldown_timer += dt


    def ProcessChargeGun(self, entity, gun, dt):
        # Active
        if gun.status == 'active':
            gun.charge_timer += dt



        # Inactive
        elif gun.status == 'inactive':
            gun.cooldown_timer += dt
