from OpenGL.GL import *
import pygame
from pygame.locals import *
from OpenGL.GLU import *


def draw_house(x, y, z):
    glTranslatef(x, y, z)
    front()
    back()
    side_right()
    side_left()
    roof_front()
    roof_back()
    roof_rightside()
    roof_leftside()
    front_door()
    back_door()
    window_left()
    window_right()

def back():

    glColor(0.9, 0.7, 0.9)
    glBegin(GL_POLYGON)
    glVertex3f(1, 10, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(15, 0, 0)
    glVertex3f(15, 10, 0)
    glEnd()

def front():

    glColor(0.9, 0.7, 0.9)
    glBegin(GL_POLYGON)
    glVertex3f(1, 10, 10)
    glVertex3f(1, 0, 10)
    glVertex3f(15, 0, 10)
    glVertex3f(15, 10, 10)
    glEnd()

def side_right():
    glColor(0.9, 0.7, 0.9)
    glBegin(GL_POLYGON)
    glVertex3f(1, 10, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(1, 0, 10)
    glVertex3f(1, 10, 10)
    glEnd()

def side_left():
    glColor(0.9, 0.7, 0.9)
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
    glColor3f(0, 0, 1)
    glBegin(GL_POLYGON)
    glVertex3f(2, 6, 10.1)
    glVertex3f(5, 6, 10.1)
    glVertex3f(5, 9, 10.1)
    glVertex3f(2, 9, 10.1)
    glEnd()
  
def window_right():
    glColor3f(0, 0, 1)
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
