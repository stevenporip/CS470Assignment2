from OpenGL.GL import *
import pygame
from pygame.locals import *
from OpenGL.GLU import *

# Draws a tree use x,y,z params to specify location
def draw_tree(x, y, z):
    # Push to apply starting transformation
    glPushMatrix()
    glTranslatef(x, y, z) # Positions to place tree
    glScalef(4, 4, 4)  # Scale the tree

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
    # Draw the street (gray road)
    glPushMatrix()
    glTranslatef(0, .2, -40) 
    glScalef(100, 0.2, 4)  
    glColor3f(0.3, 0.3, 0.3)  # Gray

    glBegin(GL_QUADS)
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(-1, 0, 1)
    glEnd()

    glPopMatrix()

    # Draw the yellow lines in the middle of the street
    line_spacing = 5  # space between each line
    line_width = 0.5  # Width of each line z axis
    line_length = 1.7  # Length of each line x axis

    glPushMatrix()
    glTranslatef(0, .3, -40)
    glColor3f(1.0, 1.0, 0.2)  # Yellow color

    # loop to draw lines on street
    for i in range(-100, 100, line_spacing):
        glBegin(GL_QUADS)
        glVertex3f(i - line_length / 2, 0, -line_width / 2)
        glVertex3f(i + line_length / 2, 0, -line_width / 2) 
        glVertex3f(i + line_length / 2, 0, line_width / 2) 
        glVertex3f(i - line_length / 2, 0, line_width / 2)
        glEnd()

    glPopMatrix()
def draw_perpendicular_street():
    glPushMatrix()
    glTranslatef(0, .2, -108) # position of the road
    glScalef(4, 0.2, 65) 
    glColor3f(0.3, 0.3, 0.3)  # Gray color

    glBegin(GL_QUADS)
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(-1, 0, 1)
    glEnd()

    glPopMatrix()


    # Draw the yellow lines in the middle of the street
    line_spacing = 5 # space between each line
    line_width = 0.5  # Width of each line z axis
    line_length = 1.7  # Length of each line x axis

    glPushMatrix()
    glTranslatef(0, .3, -108) # positioning of yellow lines
    glColor3f(1.0, 1.0, 0.2)  # Yellow color

    # loop to draw lines on the street
    for i in range(-65, 65, line_spacing):
        glBegin(GL_QUADS)
        glVertex3f(-line_width / 2, 0, i - line_length / 2)
        glVertex3f(line_width / 2, 0, i - line_length / 2)
        glVertex3f(line_width / 2, 0, i + line_length / 2)
        glVertex3f(-line_width / 2, 0, i + line_length / 2)
        glEnd()

    glPopMatrix()
def draw_palmtree(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z) # Positions to place tree
    glScalef(3,3,3)
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

def draw_traffic_light(x, y, z, current_state):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(90, 0, 1, 0)

    # Draw pole
    glColor3f(0.85, 0.85, 0.85)  # gray
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    pole = gluNewQuadric()
    gluCylinder(pole, 0.15, 0.15, 6, 20, 20)
    gluDeleteQuadric(pole)
    glPopMatrix()

    # Draw arm
    glPushMatrix()
    glTranslatef(0, 6, 0)  # Move to the top of the pole
    glRotatef(90, 0, 1, 0)
    arm = gluNewQuadric()
    gluCylinder(arm, 0.15, 0.15, 5, 20, 20)
    gluDeleteQuadric(arm)
    glPopMatrix()

    # Draw the traffic light 
    glPushMatrix()
    glTranslatef(5, 4.9, 0)  
    glColor3f(.5, .5, .5)  # Dark gray 

    # Dimensions
    width = 0.5   
    height = 1.0  
    depth = 0.2   

    glBegin(GL_QUADS)
    # Front
    glVertex3f(-width, -height, depth)
    glVertex3f(width, -height, depth)
    glVertex3f(width, height, depth)
    glVertex3f(-width, height, depth)
    # Back
    glVertex3f(-width, -height, -depth)
    glVertex3f(-width, height, -depth)
    glVertex3f(width, height, -depth)
    glVertex3f(width, -height, -depth)
    # Left
    glVertex3f(-width, -height, -depth)
    glVertex3f(-width, -height, depth)
    glVertex3f(-width, height, depth)
    glVertex3f(-width, height, -depth)
    # Right
    glVertex3f(width, -height, -depth)
    glVertex3f(width, height, -depth)
    glVertex3f(width, height, depth)
    glVertex3f(width, -height, depth)
    # Top
    glVertex3f(-width, height, -depth)
    glVertex3f(-width, height, depth)
    glVertex3f(width, height, depth)
    glVertex3f(width, height, -depth)
    # Bottom
    glVertex3f(-width, -height, -depth)
    glVertex3f(width, -height, -depth)
    glVertex3f(width, -height, depth)
    glVertex3f(-width, -height, depth)
    glEnd()

    # Draw the lights
    quadric = gluNewQuadric()
    light_positions = [0.5, 0.0, -0.5] 
    light_colors = [
        (1.0, 0.0, 0.0) if current_state == 0 else (0.3, 0.0, 0.0),  # Red
        (1.0, 1.0, 0.0) if current_state == 2 else (0.3, 0.3, 0.0),  # Yellow
        (0.0, 1.0, 0.0) if current_state == 1 else (0.0, 0.3, 0.0),  # Green
    ]

    for pos, color in zip(light_positions, light_colors):
        glPushMatrix()
        glTranslatef(0, pos, depth + 0.01) 
        glColor3f(*color)
        gluDisk(quadric, 0, 0.15, 20, 1)
        glPopMatrix()

    gluDeleteQuadric(quadric)
    glPopMatrix() 
    glPopMatrix()  
