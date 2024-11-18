from OpenGL.GL import *
import pygame
from pygame.locals import *
from OpenGL.GLU import *

# Draws a tree use x,y,z params to specify location
def draw_tree(x, y, z):
    # Push to apply starting transformation
    glPushMatrix()
    glTranslatef(x, y, z) # Positions to place tree
    glScalef(2.5, 2.5, 2.5)  # Scale the tree

    # Draw Tree Trunk
    glPushMatrix()
    glColor3f(0.55, 0.27, 0.07)  # Brown color for trunk
    glRotatef(-90, 1, 0, 0)
    trunk = gluNewQuadric()
    gluCylinder(trunk, 0.2, 0.2, 1.5, 20, 20)
    glPopMatrix()

    # Draw Leaves
    glPushMatrix()
    glColor3f(0.0, 0.5, 0.0)  # Green color for leaves
    glTranslatef(0, 1.5, 0) # First sphere location
    leaves = gluNewQuadric()
    gluSphere(leaves, 0.6, 20, 20)
    glTranslatef(0, 0.6, 0)  # Move up
    gluSphere(leaves, 0.5, 20, 20) 
    glTranslatef(0, 0.4, 0)  # Move up
    gluSphere(leaves, 0.4, 20, 20)
    glPopMatrix() 

    # Pop when tree is completed
    glPopMatrix()

def draw_street():
    glPushMatrix()
    glTranslatef(0, .2, -40) 
    glScalef(50, 0.2, 4)  
    glColor3f(0.3, 0.3, 0.3)  # Gray

    glBegin(GL_QUADS)
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(-1, 0, 1)
    glEnd()

    glPopMatrix()

def draw_palmtree(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z) # Positions to place tree
    glColor3f(0.55, 0.27, 0.07)  # Brown color for trunk
    glRotatef(-90, 1, 0, 0)
    trunk = gluNewQuadric()
    gluCylinder(trunk, 0.2, 0.2, 5.15, 20, 20)
    glTranslatef(0, 0, 5.15)
    gluDisk(trunk, 0, 0.2, 20, 1)
    glTranslatef(0, 0, -5.15)
    gluDisk(trunk, 0, 0.2, 20, 1)
    draw_leaves()
    glTranslatef(0, 0, 0.01)
    glRotatef(30, 0, 0, 1)
    draw_leaves()
    glTranslatef(0, 0, 0.01)
    glRotatef(45, 0, 0, 1)
    draw_leaves()
    glPopMatrix()

def draw_single_leaf():
    glColor(0, 1, 0)
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 5.2)
    glVertex3f(-0.3, 1, 5)
    glVertex3f(0.3, 1, 5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-0.3, 1, 5)
    glVertex3f(-0.3, 1.8, 4.6)
    glVertex3f(0, 2.5, 4)
    glVertex3f(0.3, 1.8, 4.6)
    glVertex3f(0.3, 1, 5)
    glEnd()

def draw_leaves():
    glPushMatrix()
    draw_single_leaf()
    glRotatef(60, 0, 0, 1)
    draw_single_leaf()
    glRotatef(120, 0, 0, 1)
    draw_single_leaf()
    glRotatef(180, 0, 0, 1)
    draw_single_leaf()
    glRotatef(240, 0, 0, 1)
    draw_single_leaf()
    glRotatef(300, 0, 0, 1)
    draw_single_leaf()
    glPopMatrix()

    
    

