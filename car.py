from OpenGL.GL import *
import pygame
from pygame.locals import *
from OpenGL.GLU import *


def draw_car(x, y, z):
    glTranslatef(x, y, z)
    glRotatef(90, 0, 1, 0)
    car_driver_side()
    car_pass_side()
    window1()
    window2()
    window3()
    window4()
    car_back()
    car_front()
    tire(0,-2.4,-0.2) #driver side tire
    tire(0,-6.6,-0.2) #driver side tire
    tire(0,-6.6,4.5) #passanger side tire
    tire(0,-2.4,4.5) #passanger side tire

def car_driver_side():

    glColor(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0)
    glVertex3f(9.3, 0, 0)
    glVertex3f(9.3, 2.5, 0)
    glVertex3f(7.5, 2.5, 0)
    glVertex3f(6, 4.5, 0)
    glVertex3f(1.5, 4.5, 0)
    glVertex3f(1.5, 2.5, 0)
    glVertex3f(0, 2.5, 0)
    glEnd()

def car_pass_side():

    glColor(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 5)
    glVertex3f(9.3, 0, 5)
    glVertex3f(9.3, 2.5, 5)
    glVertex3f(7.5, 2.5, 5)
    glVertex3f(6, 4.5, 5)
    glVertex3f(1.5, 4.5, 5)
    glVertex3f(1.5, 2.5, 5)
    glVertex3f(0, 2.5, 5)
    glEnd()

def window1():
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex3f(7, 2.6, 5.05)
    glVertex3f(5.8, 4.3, 5.05)
    glVertex3f(4.2, 4.3, 5.05)
    glVertex3f(4.2, 2.6, 5.05)
    glEnd()

def window2():
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex3f(7, 2.6, -0.05)
    glVertex3f(5.8, 4.3, -0.05)
    glVertex3f(4.2, 4.3, -0.05)
    glVertex3f(4.2, 2.6, -0.05)
    glEnd()

def window3(): #back window
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex3f(1.2, 2.6, 5.05)
    glVertex3f(1.7, 4.3, 5.05)
    glVertex3f(3.8, 4.3, 5.05)
    glVertex3f(3.8, 2.6, 5.05)
    glEnd()

def window4(): #back window
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex3f(1.2, 2.6, -0.05)
    glVertex3f(1.7, 4.3, -0.05)
    glVertex3f(3.8, 4.3, -0.05)
    glVertex3f(3.8, 2.6, -0.05)
    glEnd()


def car_back():
    glColor(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 5)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 2.5, 0)
    glVertex3f(1.5, 2.5, 0)
    glVertex3f(1.5, 4.5, 0)
    glVertex3f(1.5, 4.5, 5)
    glVertex3f(1.5, 2.5, 5)
    glVertex3f(0, 2.5, 5)
    
    glEnd()

def car_front():
    glColor(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex3f(9.3, 0, 5)
    glVertex3f(9.3, 0, 0)
    glVertex3f(9.3, 2.5, 0)
    glVertex3f(7.5, 2.5, 0)
    glVertex3f(6, 4.5, 0)
    glVertex3f(6, 4.5, 5)
    glVertex3f(7.5, 2.5, 5)
    glVertex3f(9.3, 2.5, 5)
    glEnd()

def tire(x,y,z):
    glPushMatrix()
    glColor(0, 0, 0)
    glRotatef(90, 0, 0, 1)
    glTranslatef(x, y, z)
    tire= gluNewQuadric()
    gluQuadricNormals(tire, GLU_SMOOTH)
    glPushMatrix()
    gluCylinder(tire, 1.15, 1.15, 1, 30, 1)
    glTranslatef(0, 0, 1)
    gluDisk(tire, 0, 1.15, 30, 1)
    glTranslatef(0, 0, -1)
    gluDisk(tire, 0, 1.15, 30, 1)
    glPopMatrix()
    glPopMatrix()