class FactorySystem():
    def __init__(self):

        pass

    def ProcessOrders(self, world):
        for key, entity in world.entity_manager.entities.iteritems():

            if entity.factory != None:
                # Create orders
                for order in entity.factory.orders:

                    # An order is a special class that contains an order name
                    # (e.g. the type of entity to be created)
                    # and an on_creation() function (described below)

                    # Get entity name and args
                    order_name = order.name

                    # Order entity
                    product = world.entity_manager.CreateEntity(order_name)

                    # Parse specifications
                    # Call the function 'on_creation', specified by the entity
                    # or system that created the original order
                    # e.g. for a bullet, the order was probably created by
                    # the shooting_action_processing_system
                    # The on_creation function's purpose is to create the order
                    # with the correct specificity; for instance, the
                    # shooting_action_processing_system will call for a bullet
                    # to be created with the correct starting position and
                    # direciton of travel; these parameters are specified
                    # by the 'on_creation' function
                    # As another example, a room is a factory that can produce
                    # orders, and specifies the location of each order
                    # with the on_creation function
                    order.on_creation(product)


                    # Attach function to on_clear that will notify the factory when cleared
                    #order.on_clear.functions.append()
                    self.AttachOnClearToProduct(entity, product)



                    # Increment number of entities out for factory
                    self.AttachProductToEntity(entity, product)




                # Done processing, clear all orders
                entity.factory.orders = []


    def AttachOnClearToProduct(self, entity, product):
        def new_on_clear_function():
            entity.factory.products


    def AttachProductToEntity(self, entity, product):
        entity.factory.products.append(product)
        entity.factory.num_products += 1
