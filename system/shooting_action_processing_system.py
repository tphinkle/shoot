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
            if gun.cooldown_timer >= gun.cooldown:

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

        bullet_specifications = {}
        bullet_specifications['x_offset'] = gun.x_offset
        bullet_specifications['y_offset'] = gun.y_offset
        bullet_specifications['direction'] = entity.orientation.facing


        order = factory_component.order(bullet_name, bullet_specifications)


        entity.factory.orders.append(order)















    def ProcessAction(self, world, dt):
        for key, entity in world.entity_manager.entitys.iteritems():
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
