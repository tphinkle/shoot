def GetTileCoords(pixel):
    x_tile = int(pixel[0]/16.)
    y_tile = int(pixel[1]/16.)
    return (x_tile, y_tile)

def GetTile(pixel, tilemap):
    x_tile, y_tile = GetTileCoords(pixel)
    return tilemap.tiles[x_tile, y_tile]

def GetBelowAdjacentTile(pixel, tilemap):
    x_tile, y_tile = GetTileCoords(pixel)
    return tilemap.tiles[x_tile, y_tile + 1]

def GetAboveAdjacentTile(pixel, tilemap):
    x_tile, y_tile = GetTileCoords(pixel)
    return tilemap.tiles[x_tile, y_tile - 1]

def GetLeftAdjacentTile(pixel, tilemap):
    x_tile, y_tile = GetTileCoords(pixel)
    return tilemap.tiles[x_tile - 1, y_tile]

def GetRightAdjacentTile(pixel, tilemap):
    x_tile, y_tile = GetTileCoords(pixel)
    return tilemap.tiles[x_tile + 1, y_tile]
