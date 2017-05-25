# Python standard library
import ctypes

# SDL
import sdl2
import sdl2.sdlimage


class RenderSystem():
    def __init__(self, sdl_renderer, window):
        self.window = window.contents
        self.sdl_renderer = sdl_renderer

    def GetWindowRect(self):
        x, y, w, h = ctypes.c_int(), ctypes.c_int(), ctypes.c_int(), ctypes.c_int()
        sdl2.SDL_GetWindowPosition(self.window, ctypes.byref(x), ctypes.byref(y))
        sdl2.SDL_GetWindowSize(self.window, ctypes.byref(w), ctypes.byref(h))
        return sdl2.SDL_Rect(x.value, y.value, w.value, h.value)


    def LoadTexture(self, filepath):
        surface = sdl2.sdlimage.IMG_Load(filepath)
        texture = sdl2.SDL_CreateTextureFromSurface(self.sdl_renderer, surface)
        sdl2.SDL_FreeSurface(surface)
        return texture

    def RenderAll(self, world):
        sdl2.SDL_RenderClear(self.sdl_renderer)


        self.RenderRoom(world)
        self.RenderEntitys(world)


        sdl2.SDL_RenderPresent(self.sdl_renderer);


    def RenderEntitys(self, world):

        camera = world.entity_manager.entitys['camera']
        camera_rect = sdl2.SDL_Rect(int(camera.position.x), int(camera.position.y),\
         camera.shape.w, camera.shape.h)
        window_rect = self.GetWindowRect()


        # Sort dictionary by z-value (render height) and render in order
        entitys = {entity.key: entity for entity in world.entity_manager.entitys.values() if entity.display != None}
        for key, entity in sorted(entitys.items(), key = lambda (k, v): v.display.z):
            self.RenderEntity(entity, camera_rect, window_rect)




    def RenderEntity(self, entity, camera_rect, window_rect):
        # Load texture if not already loaded; set texture so don't have to
        # load it again


        if entity.display.texture == None:
            entity.display.texture = self.LoadTexture(entity.display.filepath)

        x_stretch = 1.*window_rect.w/camera_rect.w
        y_stretch = 1.*window_rect.h/camera_rect.h

        x_offset = int((entity.shape.w-entity.display.source_rect.w)/2.)

        y_offset = int((entity.shape.h-entity.display.source_rect.h)/2.)



        destination_x = int((entity.position.x + x_offset - camera_rect.x)*x_stretch)
        destination_y = int((entity.position.y + y_offset - camera_rect.y)*y_stretch)
        destination_w = int(entity.display.source_rect.w*x_stretch)
        destination_h = int(entity.display.source_rect.h*y_stretch)


        destination_rect = sdl2.SDL_Rect(destination_x, destination_y, destination_w, destination_h)

        flip = sdl2.SDL_RendererFlip(sdl2.SDL_FLIP_NONE)
        if entity.orientation != None:
            if entity.orientation.facing == 'right':
                flip = sdl2.SDL_FLIP_NONE
            else:
                flip = sdl2.SDL_RendererFlip(sdl2.SDL_FLIP_HORIZONTAL)

        sdl2.SDL_RenderCopyEx(self.sdl_renderer,
                              entity.display.texture,
                              entity.display.source_rect,
                              destination_rect,
                              0,
                              None,
                              flip)


    def RenderRoom(self, world):



        camera = world.entity_manager.entitys['camera']
        camera_rect = sdl2.SDL_Rect(int(camera.position.x),\
                                    int(camera.position.y),\
                                    camera.shape.w,\
                                    camera.shape.h)
        window_rect = self.GetWindowRect()


        if world.room.display.texture == None:
            world.room.display.texture = self.LoadTexture(world.room.display.filepath)

        x_stretch = 1.*window_rect.w/camera_rect.w
        y_stretch = 1.*window_rect.h/camera_rect.h

        x_offset = int((world.room.shape.w-world.room.display.source_rect.w)/2.)

        y_offset = int((world.room.shape.h-world.room.display.source_rect.h)/2.)



        destination_x = int((x_offset - camera_rect.x)*x_stretch)
        destination_y = int((y_offset - camera_rect.y)*y_stretch)
        destination_w = int(world.room.display.source_rect.w*x_stretch)
        destination_h = int(world.room.display.source_rect.h*y_stretch)


        destination_rect = sdl2.SDL_Rect(destination_x, destination_y, destination_w, destination_h)


        flip = sdl2.SDL_RendererFlip(sdl2.SDL_FLIP_NONE)

        sdl2.SDL_RenderCopyEx(self.sdl_renderer,
                              world.room.display.texture,
                              world.room.display.source_rect,
                              destination_rect,
                              0,
                              None,
                              flip)
