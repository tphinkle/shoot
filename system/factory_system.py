class FactorySystem():
    def __init__(self):
        pass

    def ProcessOrders(self, world):
        for key, entity in world.entity_manager.entitys.iteritems():

            if entity.factory != None:
                # Create orders
                for order in entity.factory.orders:

                    # Get entity name and args
                    entity_name = order[0]
                    args = order[1]

                    # Parse arguments
                    self.ParseArguments(args)

                    # Order entity




                    # Increment number of entitys out for factory entity

                    # Attach function to on_death that will decrement upon death
                    #entity_manager.CreateOrder()


    def ParseArguments(self, args):
        # Position
        args['x_offset']
