# SDL
import sdl2

def ListToRect(listt):
    return sdl2.SDL_Rect(listt[0], listt[1], listt[2], listt[3])

def RectToList(rect):
    return [rect.x, rect.y, rect.w, rect.h]
