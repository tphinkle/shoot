class FactorySystem():
    def __init__(self):
        pass

    def ProcessOrders(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():

            if entity.factory != None:
                # Create orders
                for order in entity.factory.orders:

                    # Get entity name and args
                    entity_name = order.name


                    # Parse sepcifications
                    specifications = order.specifications
                    parsed_specificaitons = self.ParseSpecifications(entity, specifications)


                    # Order entity
                    world.entity_manager.CreateEntity(entity_name, parsed_specifications)


                    # Increment number of entitys out for factory

                    # Attach function to on_death that will decrement upon death




    def ParseSpecifications(self, entity, specifications):
        
