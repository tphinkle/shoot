# Python standard library
import sys
import ctypes
import os

# Game specific

sys.path.append('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/functions/')
import geometry

# SDL
import sdl2
import sdl2.sdlimage

#os.environ['PYSDL2_DLL_PATH'] = ''
import sdl2.sdlttf


class RenderSystem():
    def __init__(self, sdl_renderer, window):
        self.window = window.contents
        self.sdl_renderer = sdl_renderer
        self.loaded_textures = {}


    def GetWindowRect(self):
        x, y, w, h = ctypes.c_int(), ctypes.c_int(), ctypes.c_int(), ctypes.c_int()
        sdl2.SDL_GetWindowPosition(self.window, ctypes.byref(x), ctypes.byref(y))
        sdl2.SDL_GetWindowSize(self.window, ctypes.byref(w), ctypes.byref(h))
        return sdl2.SDL_Rect(x.value, y.value, w.value, h.value)


    def GetTexture(self, filepath):

        # Texture is already loaded; don't load again
        if filepath in self.loaded_textures.keys():
            texture = self.loaded_textures[filepath]

        # Texture is not loaded; load texture
        elif filepath not in self.loaded_textures.keys():
            texture = self.LoadTexture(filepath)



        return texture

    def LoadTexture(self, filepath):
        surface = sdl2.sdlimage.IMG_Load(filepath)
        texture = sdl2.SDL_CreateTextureFromSurface(self.sdl_renderer, surface)
        sdl2.SDL_FreeSurface(surface)
        self.loaded_textures[filepath] = texture

        return texture

    def RenderAll(self, world, render_dt):
        sdl2.SDL_RenderClear(self.sdl_renderer)


        self.RenderRoom(world)

        self.RenderDebug(world, render_dt)

        self.RenderEntities(world)


        sdl2.SDL_RenderPresent(self.sdl_renderer);




    def RenderDebug(self, world, render_dt):
        '''
        This probably doesn't belong here... Should move into a subsystem elsewhere.
        This is an easy light way of having a quick debugger that can print the hero's
        stats.
        Move this elsewhere later on.
        Tutorial: https://egdev.wordpress.com/2014/03/14/python-sdl2-ttf-test/
        '''

        # Open font
        font = sdl2.sdlttf.TTF_OpenFont('/home/prestonh/Desktop/Programming/gamedev/shoot/shoot/resources/fonts/computer_modern/cmunsx.ttf', 12)
        color = sdl2.SDL_Color(40,255,40)



        # Create debug text
        entity = world.entity_manager.entities['hero_0']
        debug_lines = []
        debug_lines.append('fps:' + str(round(1./render_dt)))
        debug_lines.append('(x,y):' + str(round(entity.kinematics.x,3)) +',  ' + str(round(entity.kinematics.y, 3)))
        debug_lines.append('(vx,vy):' + str(round(entity.kinematics.vx,3)) +',  ' + str(round(entity.kinematics.vy, 3)))

        debug_text = ''
        for debug_line in debug_lines:
            debug_text += debug_line + '\n'




        # Render the debug text

        # Create surface and texture
        debug_width = 200
        text_surface = sdl2.sdlttf.TTF_RenderText_Blended_Wrapped(font, debug_text, color, debug_width)
        text_texture = sdl2.SDL_CreateTextureFromSurface(self.sdl_renderer, text_surface)

        # Render surface and texture
        window_rect = self.GetWindowRect()
        w = ctypes.pointer(ctypes.c_int(0))
        h = ctypes.pointer(ctypes.c_int(0))
        sdl2.SDL_QueryTexture(text_texture, None, None, w, h)
        x = window_rect.w - debug_width
        y = 50#window_rect.h - h.contents.value
        debug_rect = sdl2.SDL_Rect(x, y, w.contents.value, h.contents.value)

        sdl2.SDL_RenderCopy(self.sdl_renderer,
                              text_texture,
                              None,
                              debug_rect)



        # Free resources
        sdl2.SDL_FreeSurface(text_surface)
        sdl2.sdlttf.TTF_CloseFont(font)




        pass

    def RenderEntities(self, world):

        camera = world.entity_manager.entities['camera_0']
        camera_rect = sdl2.SDL_Rect(int(camera.kinematics.x), int(camera.kinematics.y),\
         camera.shape.w, camera.shape.h)
        window_rect = self.GetWindowRect()


        # Sort dictionary by z-value (render height) and render in order
        for key, entity in world.entity_manager.entities.iteritems():
            if entity.display != None:


                # Only render if the entities are in the camera's scene
                if geometry.Overlapping(entity, camera):
                    self.RenderEntity(entity, camera_rect, window_rect)





    def RenderEntity(self, entity, camera_rect, window_rect):
        # Load texture if not already loaded; set texture so don't have to
        # load it again


        if entity.display.texture == None:
            entity.display.texture = self.GetTexture(entity.display.filepath)


        x_stretch = 1.*window_rect.w/camera_rect.w
        y_stretch = 1.*window_rect.h/camera_rect.h

        x_offset = int((entity.shape.w-entity.display.source_rect.w)/2.)

        y_offset = int((entity.shape.h-entity.display.source_rect.h)/2.)



        destination_x = int((entity.kinematics.x + x_offset - camera_rect.x)*x_stretch)
        destination_y = int((entity.kinematics.y + y_offset - camera_rect.y)*y_stretch)
        destination_w = int(entity.display.source_rect.w*x_stretch)
        destination_h = int(entity.display.source_rect.h*y_stretch)




        destination_rect = sdl2.SDL_Rect(destination_x, destination_y, destination_w, destination_h)

        flip = sdl2.SDL_RendererFlip(sdl2.SDL_FLIP_NONE)
        if entity.orientation != None:
            if entity.orientation.xorientation == 'right':
                flip = sdl2.SDL_FLIP_NONE
            elif entity.orientation.xorientation == 'left':
                flip = sdl2.SDL_RendererFlip(sdl2.SDL_FLIP_HORIZONTAL)

        sdl2.SDL_RenderCopyEx(self.sdl_renderer,
                              entity.display.texture,
                              entity.display.source_rect,
                              destination_rect,
                              0,
                              None,
                              flip)


    def RenderRoom(self, world):



        camera = world.entity_manager.entities['camera_0']
        camera_rect = sdl2.SDL_Rect(int(camera.kinematics.x),\
                                    int(camera.kinematics.y),\
                                    camera.shape.w,\
                                    camera.shape.h)
        window_rect = self.GetWindowRect()


        if world.room.display.texture == None:
            world.room.display.texture = self.GetTexture(world.room.display.filepath)

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
