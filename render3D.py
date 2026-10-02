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
        self.camera_movement = Vector3(0, 0, 0)
        self.arrow_rotation = Vector2(0, 0)
        self.mouse_rotating = 0
        self.camera_speed = 1/100

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
        relative_position = relative_position * Matrix.rotation_3D("y", -self.camera_rotation.y)

        if relative_position.x > 0:
            screen_position = relative_position / relative_position.x * self.screen_distance
            screen_position = Vector2(screen_position.y, screen_position.z)

            return(screen_position)

        else:

            return(False)


    def draw_point(self, position):

        screen_position = self.screen_position(position)

        if screen_position:
            coordinate = self.position + screen_position + self.size/2
            coordinate = self.to_pygame_coordinates(coordinate)

            pygame.draw.circle(self.window, self.white, coordinate.components, 2)


    def draw_line(self, position1, position2):

        screen_position = self.screen_position(position)

        if screen_position:
            coordinate = self.position + screen_position + self.size/2
            coordinate = self.to_pygame_coordinates(coordinate)

            pygame.draw.circle(self.window, self.white, coordinate.components, 2)


    def refresh(self):

        render_area_origin = self.to_pygame_coordinates(self.position + Vector2(0, self.size.y))
        render_area = pygame.Rect(render_area_origin.x, render_area_origin.y, self.size.x, self.size.y)

        pygame.draw.rect(self.window, self.black, render_area)


    def update(self, events):

        for event in events:

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_rotating = 1
                pygame.mouse.get_rel()

            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_rotating = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.camera_movement = self.camera_movement + x_unit_3D
                if event.key == pygame.K_s:
                    self.camera_movement = self.camera_movement - x_unit_3D
                if event.key == pygame.K_d:
                    self.camera_movement = self.camera_movement + y_unit_3D
                if event.key == pygame.K_a:
                    self.camera_movement = self.camera_movement - y_unit_3D
                if event.key == pygame.K_LSHIFT:
                    self.camera_movement = self.camera_movement + z_unit_3D
                if event.key == pygame.K_LCTRL:
                    self.camera_movement = self.camera_movement - z_unit_3D
                
                if event.key == pygame.K_LEFT:
                    self.arrow_rotation  = self.arrow_rotation + x_unit_2D
                if event.key == pygame.K_RIGHT:
                    self.arrow_rotation  = self.arrow_rotation - x_unit_2D
                if event.key == pygame.K_UP:
                    self.arrow_rotation  = self.arrow_rotation + y_unit_2D
                if event.key == pygame.K_DOWN:
                    self.arrow_rotation  = self.arrow_rotation - y_unit_2D

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.camera_movement = self.camera_movement - x_unit_3D
                if event.key == pygame.K_s:
                    self.camera_movement = self.camera_movement + x_unit_3D
                if event.key == pygame.K_d:
                    self.camera_movement = self.camera_movement - y_unit_3D
                if event.key == pygame.K_a:
                    self.camera_movement = self.camera_movement + y_unit_3D
                if event.key == pygame.K_LSHIFT:
                    self.camera_movement = self.camera_movement - z_unit_3D
                if event.key == pygame.K_LCTRL:
                    self.camera_movement = self.camera_movement + z_unit_3D

                if event.key == pygame.K_LEFT:
                    self.arrow_rotation  = self.arrow_rotation - x_unit_2D
                if event.key == pygame.K_RIGHT:
                    self.arrow_rotation  = self.arrow_rotation + x_unit_2D
                if event.key == pygame.K_UP:
                    self.arrow_rotation  = self.arrow_rotation - y_unit_2D
                if event.key == pygame.K_DOWN:
                    self.arrow_rotation  = self.arrow_rotation + y_unit_2D

        rotation_ammount = pygame.mouse.get_rel()
        rotation_ammount = Vector2(rotation_ammount[0], rotation_ammount[1])*self.mouse_rotating + self.arrow_rotation
        self.camera_rotation = self.camera_rotation + (rotation_ammount/10) 

        camera_movement_rotated = self.camera_movement * Matrix.rotation_3D("y", self.camera_rotation.y)
        camera_movement_rotated = camera_movement_rotated * Matrix.rotation_3D("z", self.camera_rotation.x)
        self.camera_position = self.camera_position + camera_movement_rotated * self.camera_speed
        