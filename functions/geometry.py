def Overlapping(entity0, entity1):

    # Check x overlap
    entity0_x0 = entity0.kinematics.x
    entity0_x1 = entity0.kinematics.x + entity0.shape.w
    entity1_x0 = entity1.kinematics.x
    entity1_x1 = entity1.kinematics.x + entity1.shape.w

    overlapping_x = False

    if entity0_x0 <= entity1_x0:
        if entity0_x1 >= entity1_x0:
            overlapping_x = True

    elif entity0_x0 > entity1_x0:
        if entity1_x1 >= entity0_x0:
            overlapping_x = True


    # Check y overlap
    entity0_y0 = entity0.kinematics.y
    entity0_y1 = entity0.kinematics.y + entity0.shape.h
    entity1_y0 = entity1.kinematics.y
    entity1_y1 = entity1.kinematics.y + entity1.shape.h


    overlapping_y = False

    if entity0_y0 <= entity1_y0:
        if entity0_y1 >= entity1_y0:
            overlapping_y = True

    elif entity0_y0 > entity1_y0:
        if entity1_y1 >= entity0_y0:
            overlapping_y = True


    # Check both overlap
    overlapping = False
    if overlapping_x and overlapping_y:
        overlapping = True


    return overlapping
