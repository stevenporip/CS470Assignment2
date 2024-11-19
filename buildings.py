from OpenGL.GL import *
import pygame
from pygame.locals import *
from OpenGL.GLU import *

def draw_building(x, y, z, color):
    glTranslatef(x, y, z)

    front(color)
    back(color)
    side_right(color)
    side_left(color)
    front_door()
    windows()
    windows_middle()
    windows_right()

def back(color):

    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(1, 30, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(15, 0, 0)
    glVertex3f(15, 30, 0)
    glEnd()

def front(color):

    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(1, 30, 10)
    glVertex3f(1, 0, 10)
    glVertex3f(15, 0, 10)
    glVertex3f(15, 30, 10)
    glEnd()

def side_right(color):
    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(1, 30, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(1, 0, 10)
    glVertex3f(1, 30, 10)
    glEnd()

def side_left(color):
    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(15, 0, 10)
    glVertex3f(15, 0, 0)
    glVertex3f(15, 30, 0)
    glVertex3f(15, 30, 10)
    glEnd()

def roof(color):
    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(1, 30, 10)
    glVertex3f(15, 30, 0)
    glVertex3f(15, 30, 10)
    glVertex3f(1, 30, 0)
    glEnd()

def front_door():
    glColor3f(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex3f(6, 0.0, 10.1)
    glVertex3f(10, 0.0, 10.1)
    glVertex3f(10, 5, 10.1)
    glVertex3f(6, 5, 10.1)
    glEnd()

def windows():
    glPushMatrix()
    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(2, 6, 10.1)
    glVertex3f(5, 6, 10.1)
    glVertex3f(5, 9, 10.1)
    glVertex3f(2, 9, 10.1)
    glEnd()

    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(2, 10, 10.1)
    glVertex3f(5, 10, 10.1)
    glVertex3f(5, 13, 10.1)
    glVertex3f(2, 13, 10.1)
    glEnd()

    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(2, 14, 10.1)
    glVertex3f(5, 14, 10.1)
    glVertex3f(5, 17, 10.1)
    glVertex3f(2, 17, 10.1)
    glEnd()

    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(2, 18, 10.1)
    glVertex3f(5, 18, 10.1)
    glVertex3f(5, 21, 10.1)
    glVertex3f(2, 21, 10.1)
    glEnd()

    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(2, 22, 10.1)
    glVertex3f(5, 22, 10.1)
    glVertex3f(5, 25, 10.1)
    glVertex3f(2, 25, 10.1)
    glEnd()

    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(2, 26, 10.1)
    glVertex3f(5, 26, 10.1)
    glVertex3f(5, 29, 10.1)
    glVertex3f(2, 29, 10.1)
    glEnd()

    glPopMatrix()

def windows_middle():
    glPushMatrix()
    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(6, 6, 10.1)
    glVertex3f(9, 6, 10.1)
    glVertex3f(9, 9, 10.1)
    glVertex3f(6, 9, 10.1)
    glEnd()

    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(6, 10, 10.1)
    glVertex3f(9, 10, 10.1)
    glVertex3f(9, 13, 10.1)
    glVertex3f(6, 13, 10.1)
    glEnd()

    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(6, 14, 10.1)
    glVertex3f(9, 14, 10.1)
    glVertex3f(9, 17, 10.1)
    glVertex3f(6, 17, 10.1)
    glEnd()

    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(6, 18, 10.1)
    glVertex3f(9, 18, 10.1)
    glVertex3f(9, 21, 10.1)
    glVertex3f(6, 21, 10.1)
    glEnd()

    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(6, 22, 10.1)
    glVertex3f(9, 22, 10.1)
    glVertex3f(9, 25, 10.1)
    glVertex3f(6, 25, 10.1)
    glEnd()

    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(6, 26, 10.1)
    glVertex3f(9, 26, 10.1)
    glVertex3f(9, 29, 10.1)
    glVertex3f(6, 29, 10.1)
    glEnd()

    glPopMatrix()

def windows_right():
    glPushMatrix()
    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(10, 6, 10.1)
    glVertex3f(13, 6, 10.1)
    glVertex3f(13, 9, 10.1)
    glVertex3f(10, 9, 10.1)
    glEnd()

    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(10, 10, 10.1)
    glVertex3f(13, 10, 10.1)
    glVertex3f(13, 13, 10.1)
    glVertex3f(10, 13, 10.1)
    glEnd()

    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(10, 14, 10.1)
    glVertex3f(13, 14, 10.1)
    glVertex3f(13, 17, 10.1)
    glVertex3f(10, 17, 10.1)
    glEnd()

    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(10, 18, 10.1)
    glVertex3f(13, 18, 10.1)
    glVertex3f(13, 21, 10.1)
    glVertex3f(10, 21, 10.1)
    glEnd()

    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(10, 22, 10.1)
    glVertex3f(13, 22, 10.1)
    glVertex3f(13, 25, 10.1)
    glVertex3f(10, 25, 10.1)
    glEnd()

    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_POLYGON)
    
    glVertex3f(10, 26, 10.1)
    glVertex3f(13, 26, 10.1)
    glVertex3f(13, 29, 10.1)
    glVertex3f(10, 29, 10.1)
    glEnd()

    glPopMatrix()