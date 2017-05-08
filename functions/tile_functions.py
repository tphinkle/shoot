def GetTileCoords(x, y):
    x_tile = int(x/16.)
    y_tile = int(y/16.)
    return x_tile, y_tile

def GetTile(x, y, tilemap):
    x_tile, y_tile = GetTileCoords(x,y)
    return tilemap.tiles[x_tile, y_tile]

def GetBelowTile(x, y, tilemap):
    x_tile, y_tile = GetTileCoords(x,y+1)
    return tilemap.tiles[x_tile, y_tile]

def GetAboveTile(x, y, tilemap):
    x_tile, y_tile = GetTileCoords(x,y-1)
    return tilemap.tiles[x_tile, y_tile]

def GetLeftTile(x, y, tilemap):
    x_tile, y_tile = GetTileCoords(x-1,y)
    return tilemap.tiles[x_tile, y_tile]

def GetRightTile(x, y, tilemap):
    x_tile, y_tile = GetTileCoords(x+1,y)
    return tilemap.tiles[x_tile, y_tile]
