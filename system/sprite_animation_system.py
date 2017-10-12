class SpriteAnimationSystem():
    def __init__(self):
        pass

    def UpdateEntitySprites(self, world, dt):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.sprite_animation:
                if key == 'hero':
                    self.UpdateHeroSprite(entity, dt)





    def UpdateActiveAnimation(self, entity, dt):
        # Cyclical animation
        if entity.sprite_animation.active_animation.type == 'cyclical':
            entity.sprite_animation.active_animation.clock += dt
            if entity.sprite_animation.active_animation.clock > entity.sprite_animation.active_animation.period:
                entity.sprite_animation.active_animation.clock = 0
                entity.sprite_animation.active_animation.counter = (entity.sprite_animation.active_animation.counter + 1)%entity.sprite_animation.active_animation.total_frames

        # Terminating animation
        elif entity.sprite_animation.active_animation.type == 'terminating':
            entity.sprite_animation.active_animation.clock += dt
            if entity.sprite_animation.active_animation.counter + 1 < entity.sprite_animation.active_animation.total_frames:
                if entity.sprite_animation.active_animation.clock > entity.sprite_animation.active_animation.period:
                    entity.sprite_animation.active_animation.clock = 0
                    entity.sprite_animation.active_animation.counter += 1




    def GetAnimation(self, entity, name):
        for animation in entity.sprite_animation.animations:
            if animation.name == name:
                return animation

        # Animation not found; return default
        return entity.sprite_animation.default_animation




    def SetEntitySpriteAnimation(self, entity, name, dt):


        active_name = entity.sprite_animation.active_animation.name


        # Previous action still active
        if active_name == name:
            self.UpdateActiveAnimation(entity, dt)


        # Switched action
        else:

            # Reset the active animation
            entity.sprite_animation.active_animation.clock = 0
            entity.sprite_animation.active_animation.counter = 0

            # Set the new active animation
            entity.sprite_animation.active_animation = self.GetAnimation(entity, name)


        # Change display component
        counter = entity.sprite_animation.active_animation.counter
        entity.display.source_rect = entity.sprite_animation.active_animation.rects[counter]



    '''
    Entity and action specific updates
    '''



    def UpdateHeroSprite(self, hero, dt):

        # Dashing
        if hero.dashing_action.status == 'active':
            self.SetEntitySpriteAnimation(hero, 'dashing', dt)

        # Jumping
        elif hero.jumping_action.status == 'active':
            self.SetEntitySpriteAnimation(hero, 'jumping', dt)

        



        # Running
        elif hero.running_floating_action.status == 'active':
            if hero.running_floating_action.mode == 'running':
                self.SetEntitySpriteAnimation(hero, 'running', dt)

            elif hero.running_floating_action.mode == 'floating':
                self.SetEntitySpriteAnimation(hero, 'floating', dt)




        else:
            self.SetEntitySpriteAnimation(hero, 'default', dt)



        # Floating
