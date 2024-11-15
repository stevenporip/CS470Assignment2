from OpenGL.GL import *
import pygame
from pygame.locals import *
from OpenGL.GLU import *


def draw_house(x, y, z, color):
    glTranslatef(x, y, z)
    front(color)
    back(color)
    side_right(color)
    side_left(color)
    roof_front()
    roof_back()
    roof_rightside()
    roof_leftside()
    front_door()
    back_door()
    window_left()
    window_right()

def back(color):

    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(1, 10, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(15, 0, 0)
    glVertex3f(15, 10, 0)
    glEnd()

def front(color):

    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(1, 10, 10)
    glVertex3f(1, 0, 10)
    glVertex3f(15, 0, 10)
    glVertex3f(15, 10, 10)
    glEnd()

def side_right(color):
    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(1, 10, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(1, 0, 10)
    glVertex3f(1, 10, 10)
    glEnd()

def side_left(color):
    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(15, 0, 10)
    glVertex3f(15, 0, 0)
    glVertex3f(15, 10, 0)
    glVertex3f(15, 10, 10)
    glEnd()

def roof_front():
    glColor(1, 0, 0 )
    glBegin(GL_POLYGON)
    glVertex3f(1, 10, 10)
    glVertex3f(15, 10, 10)
    glVertex3f(15, 15, 5)
    glVertex3f(1, 15, 5)
    glEnd()

def roof_back():
    glColor(1, 0, 0 )
    glBegin(GL_POLYGON)
    glVertex3f(1, 10, 0)
    glVertex3f(15, 10, 0)
    glVertex3f(15, 15, 5)
    glVertex3f(1, 15, 5)
    glEnd()

def roof_rightside():
    glColor(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex3f(15, 10, 10)
    glVertex3f(15, 10, 0)
    glVertex3f(15, 15, 5)
    glEnd()

def roof_leftside():
    glColor(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex3f(1, 10, 0)
    glVertex3f(1, 10, 10)
    glVertex3f(1, 15, 5)
    glEnd()


def front_door():
    glColor3f(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex3f(5, 0.0, 10.1)
    glVertex3f(8, 0.0, 10.1)
    glVertex3f(8, 5, 10.1)
    glVertex3f(5, 5, 10.1)
    glEnd()

def window_left():
    glColor4f(0.6, 0.8, 1.0, 0.5)
    glBegin(GL_POLYGON)
    glVertex3f(2, 6, 10.1)
    glVertex3f(5, 6, 10.1)
    glVertex3f(5, 9, 10.1)
    glVertex3f(2, 9, 10.1)
    glEnd()
  
def window_right():
    glColor4f(0.6, 0.8, 1.0, 0.5)
    glBegin(GL_POLYGON)
    glVertex3f(9, 6, 10.1)
    glVertex3f(12, 6, 10.1)
    glVertex3f(12, 9, 10.1)
    glVertex3f(9, 9, 10.1)
    glEnd()
    
def back_door():
    glColor3f(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex3f(5, 0.0, -0.1)
    glVertex3f(8, 0.0, -0.1)
    glVertex3f(8, 5, -0.1)
    glVertex3f(5, 5, -0.1)
    glEnd()
