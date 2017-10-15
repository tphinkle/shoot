# Adjacent

def GetEntityAdjLeftX(entity):
    return entity.kinematics.x - 1

def GetEntityLeftX(entity):
    return entity.kinematics.x

def GetEntityCenterX(entity):
    return entity.kinematics.x + entity.shape.w/2 - 1

def GetEntityRightX(entity):
    return entity.kinematics.x + entity.shape.w - 1

def GetEntityAdjRightX(entity):
    return entity.kinematics.x + entity .shape.w


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





















def GetEntityProposedAdjLeftX(entity):
    return entity.kinematics.x_proposed - 1

def GetEntityProposedLeftX(entity):
    return entity.kinematics.x_proposed

def GetEntityProposedCenterX(entity):
    return entity.kinematics.x_proposed + entity.shape.w/2 - 1

def GetEntityProposedRightX(entity):
    return entity.kinematics.x_proposed + entity.shape.w - 1

def GetEntityProposedAdjRightX(entity):
    return entity.kinematics.x_proposed + entity.shape.w


# Above
def GetEntityProposedAboveAdjLeftPixel(entity):
    return entity.kinematics.x_proposed - 1, entity.kinematics.y_proposed - 1

def GetEntityProposedAboveLeftPixel(entity):
    return entity.kinematics.x_proposed, entity.kinematics.y_proposed-1

def GetEntityProposedAboveCenterPixel(entity):
    return entity.kinematics.x_proposed + entity.shape.w/2-1, entity.kinematics.y_proposed-1

def GetEntityProposedAboveRightPixel(entity):
    return entity.kinematics.x_proposed + entity.shape.w-1, entity.posiition.y-1

def GetEntityProposedAboveAdjRightPixel(entity):
    return entity.kinematics.x_proposed + entity.shape.w, entity.kinematics.y_proposed - 1

def GetEntityProposedAboveY(entity):
    return entity.kinematics.y_proposed - 1

# Top

def GetEntityProposedTopAdjLeftPixel(entity):
    return entity.kinematics.x_proposed-1, entity.kinematics.y_proposed

def GetEntityProposedTopLeftPixel(entity):
    return entity.kinematics.x_proposed, entity.kinematics.y_proposed

def GetEntityProposedTopCenterPixel(entity):
    return entity.kinematics.x_proposed + entity.shape.w/2-1, entity.kinematics.y_proposed

def GetEntityProposedTopRightPixel(entity):
    return entity.kinematics.x_proposed + entity.shape.w-1, entity.kinematics.y_proposed

def GetEntityProposedTopAdjRightPixel(entity):
    return entity.kinematics.x_proposed + entity.shape.w, entity.kinematics.y_proposed

def GetEntityProposedTopY(entity):
    return entity.kinematics.y_proposed

# Middle

def GetEntityProposedMiddleAdjLeftPixel(entity):
    return entity.kinematics.x_proposed - 1, entity.kinematics.y_proposed + entity.shape.h/2 - 1

def GetEntityProposedMiddleLeftPixel(entity):
    return entity.kinematics.x_proposed, entity.kinematics.y_proposed + entity.shape.h/2 - 1

def GetEntityProposedMiddleCenterPixel(entity):
    return entity.kinematics.x_proposed + entity.shape.w/2-1, entity.kinematics.y_proposed + entity.shape.h/2-1

def GetEntityProposedMiddleRightPixel(entity):
    return entity.kinematics.x_proposed + entity.shape.w-1, entity.kinematics.y_proposed + entity.shape.h/2-1

def GetEntityProposedMiddleAdjRightPixel(entity):
    return entity.kinematics.x_proposed + entity.shape.w, entity.kinematics.y_proposed + entity.shape.h/2 - 1

def GetEntityProposedMiddleY(entity):
    return entity.kinematics.y_proposed + entity.shape.h/2-1

# Bottom

def GetEntityProposedBottomAdjLeftPixel(entity):
    return entity.kinematics.x_proposed - 1, entity.kinematics.y_proposed + entity.shape.h - 1

def GetEntityProposedBottomLeftPixel(entity):
    return entity.kinematics.x_proposed, entity.kinematics.y_proposed + entity.shape.h-1

def GetEntityProposedBottomCenterPixel(entity):
    return entity.kinematics.x_proposed + entity.shape.w/2-1, entity.kinematics.y_proposed + entity.shape.h-1

def GetEntityProposedBottomRightPixel(entity):
    return entity.kinematics.x_proposed + entity.shape.w-1, entity.kinematics.y_proposed + entity.shape.h-1

def GetEntityProposedBottomAdjRightPixel(entity):
    return entity.kinematics.x_proposed + entity.shape.w, entity.kinematics.y_proposed + entity.shape.h - 1

def GetEntityProposedBottomY(entity):
    return entity.kinematics.y_proposed + entity.shape.h - 1

# Below

def GetEntityProposedBelowAdjLeftPixel(entity):
    return entity.kinematics.x_proposed - 1, entity.kinematics.y_proposed + entity.shape.h

def GetEntityProposedBelowLeftPixel(entity):
    return entity.kinematics.x_proposed, entity.kinematics.y_proposed + entity.shape.h

def GetEntityProposedBelowCenterPixel(entity):
    return entity.kinematics.x_proposed + entity.shape.w/2-1, entity.kinematics.y_proposed + entity.shape.h

def GetEntityProposedBelowRightPixel(entity):
    return entity.kinematics.x_proposed+entity.shape.w-1, entity.kinematics.y_proposed + entity.shape.h

def GetEntityProposedBelowAdjRightPixel(entity):
    return entity.kinematics.x_proposed + entity.shape.w, entity.kinematics.y_proposed + entity.shape.h

def GetEntityProposedBelowY(entity):
    return entity.kinematics.y_proposed + entity.shape.h
