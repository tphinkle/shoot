def GetEntityAdjLeftX(entity):
    return entity.position.x - 1

def GetEntityLeftX(entity):
    return entity.position.x

def GetEntityRightX(entity):
    return entity.position.x + entity.shape.w - 1

def GetEntityAdjRightX(entity):
    return entity.position.x + entity.shape.w

# Above
def GetEntityAboveAdjLeftPixel(entity):
    return entity.position.x - 1, entity.position.y - 1

def GetEntityAboveLeftPixel(entity):
    return entity.position.x, entity.position.y-1

def GetEntityAboveCenterPixel(entity):
    return entity.position.x + entity.shape.w/2-1, entity.position.y-1

def GetEntityAboveRightPixel(entity):
    return entity.position.x + entity.shape.w-1, entity.posiition.y-1

def GetEntityAboveAdjRightPixel(entity):
    return entity.position.x + entity.shape.w, entity.position.y - 1

def GetEntityAboveY(entity):
    return entity.position.y - 1

# Top

def GetEntityTopAdjLeftPixel(entity):
    return entity.position.x-1, entity.position.y

def GetEntityTopLeftPixel(entity):
    return entity.position.x, entity.position.y

def GetEntityTopCenterPixel(entity):
    return entity.position.x + entity.shape.w/2-1, entity.position.y

def GetEntityTopRightPixel(entity):
    return entity.position.x + entity.shape.w-1, entity.position.y

def GetEntityTopAdjRightPixel(entity):
    return entity.position.x + entity.shape.w, entity.position.y

def GetEntityTopY(entity):
    return entity.position.y

# Middle

def GetEntityMiddleAdjLeftPixel(entity):
    return entity.position.x - 1, entity.position.y + entity.shape.h/2 - 1

def GetEntityMiddleLeftPixel(entity):
    return entity.position.x, entity.position.y + entity.shape.h/2 - 1

def GetEntityMiddleCenterPixel(entity):
    return entity.position.x + entity.shape.w/2-1, entity.position.y + entity.shape.h/2-1

def GetEntityMiddleRightPixel(entity):
    return entity.position.x + entity.shape.w-1, entity.position.y + entity.shape.h/2-1

def GetEntityMiddleAdjRightPixel(entity):
    return entity.position.x + entity.shape.w, entity.position.y + entity.shape.h/2 - 1

def GetEntityMiddleY(entity):
    return entity.position.y + entity.shape.h/2-1

# Bottom

def GetEntityBottomAdjLeftPixel(entity):
    return entity.position.x - 1, entity.position.y + entity.shape.h - 1

def GetEntityBottomLeftPixel(entity):
    return entity.position.x, entity.position.y + entity.shape.h-1

def GetEntityBottomCenterPixel(entity):
    return entity.position.x + entity.shape.w/2-1, entity.position.y + entity.shape.h-1

def GetEntityBottomRightPixel(entity):
    return entity.position.x + entity.shape.w-1, entity.position.y + entity.shape.h-1

def GetEntityBottomAdjRightPixel(entity):
    return entity.position.x + entity.shape.w, entity.position.y + entity.shape.h - 1

def GetEntityBottomY(entity):
    return entity.position.y + entity.shape.h - 1

# Below

def GetEntityBelowAdjLeftPixel(entity):
    return entity.position.x - 1, entity.position.y + entity.shape.h

def GetEntityBelowLeftPixel(entity):
    return entity.position.x, entity.position.y + entity.shape.h

def GetEntityBelowCenterPixel(entity):
    return entity.position.x + entity.shape.w/2-1, entity.position.y + entity.shape.h

def GetEntityBelowRightPixel(entity):
    return entity.position.x+entity.shape.w-1, entity.position.y + entity.shape.h

def GetEntityBelowAdjRightPixel(entity):
    return entity.position.x + entity.shape.w, entity.position.y + entity.shape.h

def GetEntityBelowY(entity):
    return entity.position.y + entity.shape.h
