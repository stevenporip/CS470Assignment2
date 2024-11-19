from OpenGL.GL import *
import pygame
from pygame.locals import *
from OpenGL.GLU import *


def draw_house(x, y, z, color):
    glPushMatrix()
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
    
    glPopMatrix()
    
def back(color):

    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(1, 0, 0)
    glVertex3f(6, 0, 0)
    glVertex3f(6, 10, 0)
    glVertex3f(1, 10, 0)
    glEnd()

    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(9, 0, 0)
    glVertex3f(15, 0, 0)
    glVertex3f(15, 10, 0)
    glVertex3f(9, 10, 0)
    glEnd()

    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(6, 4.5, 0)
    glVertex3f(9, 4.5, 0)
    glVertex3f(9, 10, 0)
    glVertex3f(6, 10, 0)
    glEnd()

def front(color):

    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(2, 0, 10)
    glVertex3f(2, 10, 10)
    glVertex3f(1, 10, 10)
    glVertex3f(1, 0, 10)
    glEnd()

    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(2, 10, 10)
    glVertex3f(2, 9, 10)
    glVertex3f(14, 9, 10)
    glVertex3f(14, 10, 10)
    glEnd()

    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(14, 0, 10)
    glVertex3f(15, 0, 10)
    glVertex3f(15, 10, 10)
    glVertex3f(14, 10, 10)
    glEnd()

    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(6, 4.5, 10)
    glVertex3f(9, 4.5, 10)
    glVertex3f(9, 9, 10)
    glVertex3f(6, 9, 10)
    glEnd()

    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(2, 0, 10)
    glVertex3f(6, 0, 10)
    glVertex3f(6, 5, 10)
    glVertex3f(2, 5, 10)
    glEnd()
    
    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(9, 0, 10)
    glVertex3f(14, 0, 10)
    glVertex3f(14, 5, 10)
    glVertex3f(9, 5, 10)
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
    glVertex3f(6, 0.0, 10)
    glVertex3f(9, 0.0, 10)
    glVertex3f(9, 4.5, 10)
    glVertex3f(6, 4.5, 10)
    glEnd()


    
def back_door():
    glColor3f(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex3f(6, 0.0, 0)
    glVertex3f(9, 0.0, 0)
    glVertex3f(9, 4.5, 0)
    glVertex3f(6, 4.5, 0)
    glEnd()
