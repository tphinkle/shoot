def GetEntityCenterCoords(entity):
    return (entity.position.x + entity.shape.w/2.,\
            entity.position.y + entity.shape.h/2.)


def GetEntityTopLeftPixel(entity):
    return entity.position.x, entity.position.y

def GetEntityTopRightPixel(entity):
    return entity.position.x + entity.shape.w, entity.position.y

def GetEntityBottomLeftPixel(entity):
    return entity.position.x, entity.position.y + entity.shape.h

def GetEntityBottomRightPixel(entity):
    return entity.position.x + entity.shape.w, entity.position.y + entity.shape.h

def GetEntityBottomY(entity):
    return entity.position.y + entity.shape.h
