from OpenGL.GL import *
import pygame
from pygame.locals import *
from OpenGL.GLU import *


def draw_boat(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    boat_backside_left()
    boat_backside_right()
    boat_bottom()
    boat_leftside()
    boat_rightside()
    boat_leftside_point()
    boat_rightside_point()
    sail_rod()
    boat_sail1()
    boat_sail2()
    glPopMatrix()

def boat_backside_left():

    glColor(0.55, 0.27, 0.07)
    glBegin(GL_POLYGON)
    glVertex3f(-3, 0, 2.5)
    glVertex3f(-3, 2.5, 2.5)
    glVertex3f(0, 2.5, 0)
    glVertex3f(0, 0, 0)
    glEnd()

def boat_backside_right():
    glColor(0.55, 0.27, 0.07)
    glBegin(GL_POLYGON)
    glVertex3f(-3, 0, 2.5)
    glVertex3f(-3, 2.5, 2.5)
    glVertex3f(0, 2.5, 5)
    glVertex3f(0, 0, 5)
    glEnd()

def boat_bottom():

    glColor(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex3f(0, 0.1, 5)
    glVertex3f(-3, 0.1, 2.5)
    glVertex3f(0, 0.1, 0)
    glVertex3f(12, 0.1, 0)
    glVertex3f(15, 0.1, 2.5)
    glVertex3f(12, 0.1, 5)
    glEnd()

def boat_leftside():

    glColor(0.55, 0.27, 0.07)
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 2.5, 0)
    glVertex3f(12, 2.5, 0)
    glVertex3f(12, 0, 0)
    glEnd()

def boat_leftside_point():

    glColor(0.55, 0.27, 0.07)
    glBegin(GL_POLYGON)
    glVertex3f(15, 0, 2.5)
    glVertex3f(15, 2.5, 2.5)
    glVertex3f(12, 2.5, 0)
    glVertex3f(12, 0, 0)
    glEnd()

def boat_rightside():
    glColor(0.55, 0.27, 0.07)
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 5)
    glVertex3f(0, 2.5, 5)
    glVertex3f(12, 2.5, 5)
    glVertex3f(12, 0, 5)
    glEnd()

def boat_rightside_point():
    glColor(0.55, 0.27, 0.07)
    glBegin(GL_POLYGON)
    glVertex3f(15, 0, 2.5)
    glVertex3f(15, 2.5, 2.5)
    glVertex3f(12, 2.5, 5)
    glVertex3f(12, 0, 5)
    glEnd()

def sail_rod():
    glPushMatrix()
    glTranslatef(5, 0.1, 2.5)
    glColor(0.55, 0.27, 0.07)
    glRotatef(-90, 1, 0, 0)
    trunk = gluNewQuadric()
    gluCylinder(trunk, 0.2, 0.2, 12, 20, 20)
    glTranslatef(0, 0, 12)
    gluDisk(trunk, 0, 0.2, 20, 1)
    glPopMatrix()

def boat_sail1():
    glColor(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex3f(5, 3.5, 2.5)
    glVertex3f(5, 12, 2.5)
    glVertex3f(-1, 3.5, 2.5)
    glEnd()

def boat_sail2():
    glColor(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex3f(5, 3.5, 2.5)
    glVertex3f(5, 10, 2.5)
    glVertex3f(12, 3.5, 2.5)
    glEnd()



