# Python standard library
import sys

# Game specific
sys.path.append('../component/')
import factory_component

import helper_systems

class ShootingActionProcessingSystem(helper_systems.Subject):



    def __init__(self):

        # Initialize observer class
        helper_systems.Subject.__init__(self)

        pass

    def InterpretRawCommand(self, raw_command):
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

                # NotifyObservers gun shot
                self.NotifyObservers(entity, gun.name + 'fired')

                # Fire gun
                self.FireGun(entity, gun)

                # Set to inactive status
                gun.status = 'inactive'


        # Stop
        elif action['trigger'] == 'stop':
            pass





    def TriggerChargeShot(self, entity, gun, action):
        # Start
        if action['trigger'] == 'start':
            gun.status = 'active'


        # Stop
        elif action['trigger'] == 'stop':


            # Make sure charged long enough to actually fire a shot
            if gun.charge_timer >= gun.charge_times[0]:


                # Find correct bullet to shoot
                for i in range(len(gun.bullet_names)):
                    if gun.charge_timer > gun.charge_times[i]:
                        gun.bullet_name = gun.bullet_names[i]



                # Fire gun
                if gun.bullets_out < gun.max_bullets_out:
                    self.NotifyObservers(entity, gun.name + 'fired')
                    self.FireGun(entity, gun)



            # Update status
            gun.bullet_name = None
            gun.charge_timer = 0
            gun.status = 'inactive'



    def FireGun(self, entity, gun):


        # Reset timer
        gun.cooldown_timer = 0


        # Get bullet name
        bullet_name = gun.bullet_name




        # Create specifications for bullet
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


            # Add on clear component
            def ResetBullets():
                gun.bullets_out = gun.bullets_out - 1
            new_bullet.on_clear.functions.append(ResetBullets)



        # Create order and send to factory
        order = factory_component.Order(bullet_name, on_creation)
        entity.factory.orders.append(order)




        # Notify observers
        self.NotifyObservers(entity, bullet_name + 'fired')







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
            self.NotifyObservers(entity, gun.name + 'active')
            pass

        # Inactive
        elif gun.status == 'inactive':
            self.NotifyObservers(entity, gun.name + 'inactive')
            gun.cooldown_timer += dt


    def ProcessChargeGun(self, entity, gun, dt):
        # Active
        if gun.status == 'active':
            self.NotifyObservers(entity, gun.name + 'active')
            gun.charge_timer += dt



        # Inactive
        elif gun.status == 'inactive':
            self.NotifyObservers(entity, gun.name + 'inactive')
            gun.cooldown_timer += dt
