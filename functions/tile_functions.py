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
