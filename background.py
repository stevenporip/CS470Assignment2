from OpenGL.GL import *
import pygame
from pygame.locals import *

def load_texture(filename):
    texture_surface = pygame.image.load(filename)
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
    width, height = texture_surface.get_rect().size

    glEnable(GL_TEXTURE_2D)
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    return texture

def draw_ground(texture):
    glPushMatrix()
    glTranslatef(0, 0.1, -70)  
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-100, 0, -100)
    glTexCoord2f(1, 0); glVertex3f(100, 0, -100)
    glTexCoord2f(1, 1); glVertex3f(100, 0, 100)
    glTexCoord2f(0, 1); glVertex3f(-100, 0, 100)
    glEnd()
    glPopMatrix()

def draw_water(texture):
    glPushMatrix()
    glTranslatef(0, 0, 90)  
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-100, 0, -30)
    glTexCoord2f(1, 0); glVertex3f(100, 0, -30)
    glTexCoord2f(1, 1); glVertex3f(100, 0, 30)
    glTexCoord2f(0, 1); glVertex3f(-100, 0, 30)
    glEnd()
    glPopMatrix()

def draw_sand(texture):
    glPushMatrix()
    glTranslatef(0, 0, 0)  
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-100, 0, -60)
    glTexCoord2f(1, 0); glVertex3f(100, 0, -60)
    glTexCoord2f(1, 1); glVertex3f(100, 0, 60)
    glTexCoord2f(0, 1); glVertex3f(-100, 0, 60)
    glEnd()
    glPopMatrix()
