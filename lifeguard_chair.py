from OpenGL.GL import *
import pygame
from pygame.locals import *
from OpenGL.GLU import *


def draw_lifeguardchair(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glScale(0.6,0.6,0.6)
    seat()
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    glTranslatef(0,-5,5)
    seat()
    glPopMatrix()
    glPushMatrix()
    seat_vertical()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(5,0,5)
    seat_vertical()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0,0,5)
    seat_vertical()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(5,0,0)
    seat_vertical()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0,3,0)
    seat_horizontial()
    glTranslatef(5,0,0)
    seat_horizontial()
    glRotatef(-90,0,1,0)
    seat_horizontial()
    glPopMatrix()
    glPushMatrix()
    glRotatef(90,0,1,0)
    glTranslatef(-5,2,0)
    seat_horizontial()
    glTranslatef(0,2,0)
    seat_horizontial()
    glPopMatrix()
    glTranslatef(0,8,0)
    seat_armrest()
    glTranslatef(5,0,0)
    seat_armrest()
    glPopMatrix()

def seat():
    glPushMatrix()
    seat_top()
    seat_side()
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    seat_side()
    glPopMatrix()
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    glTranslatef(-5, 0, 0)
    seat_side()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(5, 0, 0)
    seat_side()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0, -1, 0)
    seat_top()
    glPopMatrix()
    glPopMatrix()


def seat_top():
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex3f(0, 6, 5)
    glVertex3f(0, 6, 0)
    glVertex3f(5, 6, 0)
    glVertex3f(5, 6, 5)
    glEnd()

def seat_side():
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex3f(0, 6, 5)
    glVertex3f(0, 6, 0)
    glVertex3f(0, 5, 0)
    glVertex3f(0, 5, 5)
    glEnd()

def seat_vertical():
    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glRotatef(-90, 1, 0, 0)
    rod = gluNewQuadric()
    gluCylinder(rod, 0.2, 0.2, 8, 20, 20)
    glTranslatef(0, 0, 8)
    gluDisk(rod, 0, 0.2, 20, 1)
    glPopMatrix()

def seat_horizontial():
    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    rod = gluNewQuadric()
    gluCylinder(rod, 0.2, 0.2, 5, 20, 20)
    glPopMatrix()

def seat_armrest():
    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    armrest = gluNewQuadric()
    gluCylinder(armrest, 0.2, 0.2, 5, 20, 20)
    glTranslatef(0, 0, 5)
    gluDisk(armrest, 0, 0.2, 20, 1)
    glTranslatef(0, 0, -5)
    gluDisk(armrest, 0, 0.2, 20, 1)
    glPopMatrix()