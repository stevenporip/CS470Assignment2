from OpenGL.GL import *
import pygame
from pygame.locals import *
from OpenGL.GLU import *

def draw_mountain(base_size, height, position):
    glPushMatrix()
    glTranslatef(position[0], position[1], position[2])

    # Front face
    glColor3f(0.5, 0.35, 0.05)
    glBegin(GL_TRIANGLES)
    glVertex3f(0, height, 0)
    glVertex3f(-base_size / 2, 0, base_size / 2) 
    glVertex3f(base_size / 2, 0, base_size / 2)

    # Right face 
    glColor3f(0.7, 0.5, 0.2)  
    glVertex3f(0, height, 0) 
    glVertex3f(base_size / 2, 0, base_size / 2) 
    glVertex3f(base_size / 2, 0, -base_size / 2) 

    # Back face 
    glColor3f(0.8, 0.6, 0.3) 
    glVertex3f(0, height, 0) 
    glVertex3f(base_size / 2, 0, -base_size / 2) 
    glVertex3f(-base_size / 2, 0, -base_size / 2) 

    # Left face
    glColor3f(0.3, 0.2, 0.1) 
    glVertex3f(0, height, 0) 
    glVertex3f(-base_size / 2, 0, -base_size / 2) 
    glVertex3f(-base_size / 2, 0, base_size / 2)

    glEnd()

    glPopMatrix()
