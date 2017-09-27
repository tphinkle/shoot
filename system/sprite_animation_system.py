class SpriteAnimationSystem():
    def __init__(self):
        pass

    def UpdateEntitySprites(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():
            if entity.sprite_animation_component != None:

                # For entities with multiple actions corresponding to sprite changes
                if key == 'hero':
                    self.UpdateHeroSprite(hero)




                # For non-acting entities that still cycle sprites


    def UpdateHeroSprite(self, hero):
        # Running

        # Floating

        # Dashing
