class FactorySystem():
    def __init__(self):
        pass

    def ProcessOrders(world):
        for entity in world.entity_manager.entitys:
            if entity.factory != None:
                # Create orders
                for order, specifications in entity.factory.orders.iteritems():
                    world.entity_manager.CreateEntity(order, specifications)
