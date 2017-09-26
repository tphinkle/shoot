

def GetEntityAdjLeftX(entity):
    return entity.kinematics.x - 1

def GetEntityLeftX(entity):
    return entity.kinematics.x

def GetEntityCenterX(entity):
    return entity.kinematics.x + entity.shape.w/2 - 1

def GetEntityRightX(entity):
    return entity.kinematics.x + entity.shape.w - 1

def GetEntityAdjRightX(entity):
    return entity.kinematics.x + entity.shape.w


# Above
def GetEntityAboveAdjLeftPixel(entity):
    return entity.kinematics.x - 1, entity.kinematics.y - 1

def GetEntityAboveLeftPixel(entity):
    return entity.kinematics.x, entity.kinematics.y-1

def GetEntityAboveCenterPixel(entity):
    return entity.kinematics.x + entity.shape.w/2-1, entity.kinematics.y-1

def GetEntityAboveRightPixel(entity):
    return entity.kinematics.x + entity.shape.w-1, entity.posiition.y-1

def GetEntityAboveAdjRightPixel(entity):
    return entity.kinematics.x + entity.shape.w, entity.kinematics.y - 1

def GetEntityAboveY(entity):
    return entity.kinematics.y - 1

# Top

def GetEntityTopAdjLeftPixel(entity):
    return entity.kinematics.x-1, entity.kinematics.y

def GetEntityTopLeftPixel(entity):
    return entity.kinematics.x, entity.kinematics.y

def GetEntityTopCenterPixel(entity):
    return entity.kinematics.x + entity.shape.w/2-1, entity.kinematics.y

def GetEntityTopRightPixel(entity):
    return entity.kinematics.x + entity.shape.w-1, entity.kinematics.y

def GetEntityTopAdjRightPixel(entity):
    return entity.kinematics.x + entity.shape.w, entity.kinematics.y

def GetEntityTopY(entity):
    return entity.kinematics.y

# Middle

def GetEntityMiddleAdjLeftPixel(entity):
    return entity.kinematics.x - 1, entity.kinematics.y + entity.shape.h/2 - 1

def GetEntityMiddleLeftPixel(entity):
    return entity.kinematics.x, entity.kinematics.y + entity.shape.h/2 - 1

def GetEntityMiddleCenterPixel(entity):
    return entity.kinematics.x + entity.shape.w/2-1, entity.kinematics.y + entity.shape.h/2-1

def GetEntityMiddleRightPixel(entity):
    return entity.kinematics.x + entity.shape.w-1, entity.kinematics.y + entity.shape.h/2-1

def GetEntityMiddleAdjRightPixel(entity):
    return entity.kinematics.x + entity.shape.w, entity.kinematics.y + entity.shape.h/2 - 1

def GetEntityMiddleY(entity):
    return entity.kinematics.y + entity.shape.h/2-1

# Bottom

def GetEntityBottomAdjLeftPixel(entity):
    return entity.kinematics.x - 1, entity.kinematics.y + entity.shape.h - 1

def GetEntityBottomLeftPixel(entity):
    return entity.kinematics.x, entity.kinematics.y + entity.shape.h-1

def GetEntityBottomCenterPixel(entity):
    return entity.kinematics.x + entity.shape.w/2-1, entity.kinematics.y + entity.shape.h-1

def GetEntityBottomRightPixel(entity):
    return entity.kinematics.x + entity.shape.w-1, entity.kinematics.y + entity.shape.h-1

def GetEntityBottomAdjRightPixel(entity):
    return entity.kinematics.x + entity.shape.w, entity.kinematics.y + entity.shape.h - 1

def GetEntityBottomY(entity):
    return entity.kinematics.y + entity.shape.h - 1

# Below

def GetEntityBelowAdjLeftPixel(entity):
    return entity.kinematics.x - 1, entity.kinematics.y + entity.shape.h

def GetEntityBelowLeftPixel(entity):
    return entity.kinematics.x, entity.kinematics.y + entity.shape.h

def GetEntityBelowCenterPixel(entity):
    return entity.kinematics.x + entity.shape.w/2-1, entity.kinematics.y + entity.shape.h

def GetEntityBelowRightPixel(entity):
    return entity.kinematics.x+entity.shape.w-1, entity.kinematics.y + entity.shape.h

def GetEntityBelowAdjRightPixel(entity):
    return entity.kinematics.x + entity.shape.w, entity.kinematics.y + entity.shape.h

def GetEntityBelowY(entity):
    return entity.kinematics.y + entity.shape.h
