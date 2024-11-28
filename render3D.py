from vectors import *
from math import sin, cos, pi
import pygame



class Render3D:
    
    def __init__(self, window, position, size):

        self.window = window
        self.window_size = window.get_size()

        self.position = position
        self.size = size
        
        self.camera_position = Vector3(0, 0, 0)
        self.camera_rotation = Vector2(0, 0)

        self.FOV = pi * 4/6
        self.screen_distance = (size.x/2)*cos(self.FOV/2)/sin(self.FOV/2)

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)


    def to_pygame_coordinates(self, coordinate):

        result = Vector2(coordinate.x, self.window_size[1] - coordinate.y)
        return(result)


    def screen_position(self, position):

        relative_position = (position - self.camera_position)
        relative_position = relative_position * Matrix.rotation_3D("z", -self.camera_rotation.x)
        relative_position = relative_position * Matrix.rotation_3D("x", -self.camera_rotation.y)

        if relative_position.x > 0:
            screen_position = relative_position / relative_position.x * self.screen_distance
        screen_position = Vector2(screen_position.y, screen_position.z)

        return(screen_position)


    def draw_point(self, position):

        coordinate = self.position + self.screen_position(position) + self.size/2
        coordinate = self.to_pygame_coordinates(coordinate)

        pygame.draw.circle(self.window, self.white, coordinate.components, 2)


    def refresh(self):

        render_area_origin = self.to_pygame_coordinates(self.position + Vector2(0, self.size.y))
        render_area = pygame.Rect(render_area_origin.x, render_area_origin.y, self.size.x, self.size.y)

        pygame.draw.rect(self.window, self.black, render_area)

        

        