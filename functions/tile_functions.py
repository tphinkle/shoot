import coord_transforms

def GetTileCoords(pixel):
    x_tile = int(pixel[0]/16.)
    y_tile = int(pixel[1]/16.)
    return (x_tile, y_tile)

def GetTile(pixel, tilemap):
    x_tile, y_tile = GetTileCoords(pixel)
    #print 'pixel:', pixel
    #print 'tile:', y_tile, x_tile
    return tilemap.tiles[y_tile, x_tile]

def GetBelowAdjacentTile(pixel, tilemap):
    x_tile, y_tile = GetTileCoords(pixel)
    return tilemap.tiles[y_tile + 1, x_tile]

def GetAboveAdjacentTile(pixel, tilemap):
    x_tile, y_tile = GetTileCoords(pixel)
    return tilemap.tiles[y_tile - 1, x_tile]

def GetLeftAdjacentTile(pixel, tilemap):
    x_tile, y_tile = GetTileCoords(pixel)
    return tilemap.tiles[y_tile, x_tile - 1]

def GetRightAdjacentTile(pixel, tilemap):
    x_tile, y_tile = GetTileCoords(pixel)
    return tilemap.tiles[x_tile + 1, y_tile]

def GetEntityBelowCenterTile(entity, world):
    below_center_pixel = coord_transforms.GetEntityBelowCenterPixel(entity)
    below_center_tile = GetTile(below_center_pixel, world.room.tilemap)

    return below_center_tile

def CheckEntityGrounded(world, entity):
    below_left_pixel = coord_transforms.GetEntityBelowLeftPixel(entity)
    below_right_pixel = coord_transforms.GetEntityBelowRightPixel(entity)

    below_left_tile = GetTile(below_left_pixel, world.room.tilemap)
    below_right_tile = GetTile(below_right_pixel, world.room.tilemap)



    if below_left_tile.type == 'solid' or below_right_tile.type == 'solid':
        return True
    else:
        return False
