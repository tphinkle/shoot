class FactorySystem():
    def __init__(self):

        pass

    def ProcessOrders(self, world):
        for key, entity in world.entity_manager.entities.iteritems():

            if entity.factory != None:
                # Create orders
                for order in entity.factory.orders:

                    # Get entity name and args
                    entity_name = order.name


                    # Parse sepcifications
                    on_creation = order.on_creation

                    # Order entity
                    new_entity = world.entity_manager.CreateEntity(entity_name)

                    # Attach components
                    on_creation(new_entity)

                    # Increment number of entities out for factory
                    entity.factory.num_products += 1


                    # Attach function to on_death that will decrement upon death

                entity.factory.orders = []
