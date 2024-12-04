from OpenGL.GL import *
import pygame
from OpenGL.raw.GLUT import glutSolidCube, glutSolidSphere
from pygame.locals import *
from OpenGL.GLU import *
import math
import time
start_time = time.time()

def draw_lifeguard(x, y, z, torso_color, color):
    glPushMatrix()

    #Light setup
    light_position = [x+6, y+12, z, 1.0]
    light_diffuse = [0.8, 0.8, 0.8, 1.0]
    mat_diffuse = [0.969, 0.925, 0.8, 1.0]

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glPopMatrix()
    glPushMatrix()

    glTranslatef(x, y, z)

    # Timer check for waving and rotation
    elapsed_time = time.time() - start_time
    rotating = elapsed_time > 15

    # Apply rotation after 15 seconds

    if rotating:
        angle = (elapsed_time - 15) * 10  # Rotate more as time passes
        if angle > 180: # stop rotating at 180 degrees
            angle = 180
        glRotatef(angle, 0, 1, 0)  # Rotate the whole body around the Y-axis

    left_leg(color)
    right_leg(color)
    left_arm(color)
    right_arm(color)
    torso(torso_color)
    head(color)

    glPopMatrix()

def left_leg(color):
    glColor(color)
    glPushMatrix()
    glTranslatef(-0.80, 0.0, 0.0)  # Adjust to stand on y = 0
    glBegin(GL_QUADS)

    # Front face
    glVertex3f(-0.75, 0, 0.75)
    glVertex3f(0.75, 0, 0.75)
    glVertex3f(0.75, 2.0, 0.75)
    glVertex3f(-0.75, 2.0, 0.75)

    # Back face
    glVertex3f(-0.75, 0, -0.75)
    glVertex3f(0.75, 0, -0.75)
    glVertex3f(0.75, 2.0, -0.75)
    glVertex3f(-0.75, 2.0, -0.75)

    # Left face
    glVertex3f(-0.75, 0, -0.75)
    glVertex3f(-0.75, 0, 0.75)
    glVertex3f(-0.75, 2.0, 0.75)
    glVertex3f(-0.75, 2.0, -0.75)

    glColor(255,255,255)
    # Right face
    glVertex3f(0.75, 0, -0.75)
    glVertex3f(0.75, 0, 0.75)
    glVertex3f(0.75, 2.0, 0.75)
    glVertex3f(0.75, 2.0, -0.75)

    glColor(color)
    # Top face
    glVertex3f(-0.75, 2.0, -0.75)
    glVertex3f(0.75, 2.0, -0.75)
    glVertex3f(0.75, 2.0, 0.75)
    glVertex3f(-0.75, 2.0, 0.75)

    # Bottom face
    glVertex3f(-0.75, 0, -0.75)
    glVertex3f(0.75, 0, -0.75)
    glVertex3f(0.75, 0, 0.75)
    glVertex3f(-0.75, 0, 0.75)

    glEnd()
    glPopMatrix()


def right_leg(color):
    glColor(color)
    glPushMatrix()
    glTranslatef(0.80, 0.0, 0.0)  # Adjust to stand on y = 0
    glBegin(GL_QUADS)

    # Repeat the same process as left_leg
    # Front face
    glVertex3f(-0.75, 0, 0.75)
    glVertex3f(0.75, 0, 0.75)
    glVertex3f(0.75, 2.0, 0.75)
    glVertex3f(-0.75, 2.0, 0.75)

    # Back face
    glVertex3f(-0.75, 0, -0.75)
    glVertex3f(0.75, 0, -0.75)
    glVertex3f(0.75, 2.0, -0.75)
    glVertex3f(-0.75, 2.0, -0.75)

    glColor(255,255,255)
    # Left face
    glVertex3f(-0.75, 0, -0.75)
    glVertex3f(-0.75, 0, 0.75)
    glVertex3f(-0.75, 2.0, 0.75)
    glVertex3f(-0.75, 2.0, -0.75)

    glColor(color)
    # Right face
    glVertex3f(0.75, 0, -0.75)
    glVertex3f(0.75, 0, 0.75)
    glVertex3f(0.75, 2.0, 0.75)
    glVertex3f(0.75, 2.0, -0.75)

    # Top face
    glVertex3f(-0.75, 2.0, -0.75)
    glVertex3f(0.75, 2.0, -0.75)
    glVertex3f(0.75, 2.0, 0.75)
    glVertex3f(-0.75, 2.0, 0.75)

    # Bottom face
    glVertex3f(-0.75, 0, -0.75)
    glVertex3f(0.75, 0, -0.75)
    glVertex3f(0.75, 0, 0.75)
    glVertex3f(-0.75, 0, 0.75)

    glEnd()
    glPopMatrix()

def left_arm(color):
    glColor(color)
    glPushMatrix()
    glTranslatef(-2.25, 2.0, 0.0)  # Position the left arm relative to the torso
    glBegin(GL_QUADS)

    # Front face
    glVertex3f(-0.75, 0, 0.75)
    glVertex3f(0.75, 0, 0.75)
    glVertex3f(0.75, 2.0, 0.75)
    glVertex3f(-0.75, 2.0, 0.75)

    # Back face
    glVertex3f(-0.75, 0, -0.75)
    glVertex3f(0.75, 0, -0.75)
    glVertex3f(0.75, 2.0, -0.75)
    glVertex3f(-0.75, 2.0, -0.75)

    # Left face
    glVertex3f(-0.75, 0, -0.75)
    glVertex3f(-0.75, 0, 0.75)
    glVertex3f(-0.75, 2.0, 0.75)
    glVertex3f(-0.75, 2.0, -0.75)

    # Right face
    glVertex3f(0.75, 0, -0.75)
    glVertex3f(0.75, 0, 0.75)
    glVertex3f(0.75, 2.0, 0.75)
    glVertex3f(0.75, 2.0, -0.75)

    # Top face
    glVertex3f(-0.75, 2.0, -0.75)
    glVertex3f(0.75, 2.0, -0.75)
    glVertex3f(0.75, 2.0, 0.75)
    glVertex3f(-0.75, 2.0, 0.75)

    # Bottom face
    glVertex3f(-0.75, 0, -0.75)
    glVertex3f(0.75, 0, -0.75)
    glVertex3f(0.75, 0, 0.75)
    glVertex3f(-0.75, 0, 0.75)

    glEnd()
    glPopMatrix()

def right_arm(color, waving = False):
    glColor(color)
    glPushMatrix()
    glTranslatef(2.25, 2.0, 0.0)  # Position the right arm relative to the torso

    elapsed_time = time.time() - start_time
    if elapsed_time > 15:  # if 15 seconds have passed, start animation
        waving = True
    else:
        waving = False
    # If waving, animate the arm to move up and down
    if waving:
        # Move the arm upwards, with some oscillation for waving
        angle = 45 + 15 * math.sin(time.time() * 2) #math for the angle to wave at and smoothly wave

        # Rotate the arm upwards and to the side
        glRotatef(angle, 1, 0, -2)

    else:
        # Default position if not waving
        glRotatef(0, 1, 0, 0)
    glBegin(GL_QUADS)

    # Front face
    glVertex3f(-0.75, 0, 0.75)
    glVertex3f(0.75, 0, 0.75)
    glVertex3f(0.75, 2.0, 0.75)
    glVertex3f(-0.75, 2.0, 0.75)

    # Back face
    glVertex3f(-0.75, 0, -0.75)
    glVertex3f(0.75, 0, -0.75)
    glVertex3f(0.75, 2.0, -0.75)
    glVertex3f(-0.75, 2.0, -0.75)

    # Left face
    glVertex3f(-0.75, 0, -0.75)
    glVertex3f(-0.75, 0, 0.75)
    glVertex3f(-0.75, 2.0, 0.75)
    glVertex3f(-0.75, 2.0, -0.75)

    # Right face
    glVertex3f(0.75, 0, -0.75)
    glVertex3f(0.75, 0, 0.75)
    glVertex3f(0.75, 2.0, 0.75)
    glVertex3f(0.75, 2.0, -0.75)

    # Top face
    glVertex3f(-0.75, 2.0, -0.75)
    glVertex3f(0.75, 2.0, -0.75)
    glVertex3f(0.75, 2.0, 0.75)
    glVertex3f(-0.75, 2.0, 0.75)

    # Bottom face
    glVertex3f(-0.75, 0, -0.75)
    glVertex3f(0.75, 0, -0.75)
    glVertex3f(0.75, 0, 0.75)
    glVertex3f(-0.75, 0, 0.75)

    glEnd()
    glPopMatrix()

def torso(color):
    glColor(color)
    glPushMatrix()
    glTranslatef(0.0, 2.0, 0.0)  # Position torso on top of legs
    glBegin(GL_QUADS)

    # Front face
    x = 1.5
    z = 1.5
    glVertex3f(-x, 0, z)
    glVertex3f(x, 0, z)
    glVertex3f(x, 2.0, z)
    glVertex3f(-x, 2.0, z)

    # Back face
    glVertex3f(-x, 0, -z)
    glVertex3f(x, 0, -z)
    glVertex3f(x, 2.0, -z)
    glVertex3f(-x, 2.0, -z)

    # Left face
    glVertex3f(-x, 0, -z)
    glVertex3f(-x, 0, z)
    glVertex3f(-x, 2.0, z)
    glVertex3f(-x, 2.0, -z)

    # Right face
    glVertex3f(x, 0, -z)
    glVertex3f(x, 0, z)
    glVertex3f(x, 2.0, z)
    glVertex3f(x, 2.0, -z)

    # Top face
    glVertex3f(-x, 2.0, -z)
    glVertex3f(x, 2.0, -z)
    glVertex3f(x, 2.0, z)
    glVertex3f(-x, 2.0, z)

    # Bottom face
    glVertex3f(-x, 0, -z)
    glVertex3f(x, 0, -z)
    glVertex3f(x, 0, z)
    glVertex3f(-x, 0, z)

    glEnd()
    glPopMatrix()


def head(color):
    glColor(color)
    glPushMatrix()
    glTranslatef(0.0, 4.0, 0.0)  # Position the head above the torso
    glBegin(GL_QUADS)
    # Front face
    x = 0.75
    z = 0.75
    glVertex3f(-x, 0, z)
    glVertex3f(x, 0, z)
    glVertex3f(x, 1.0, z)
    glVertex3f(-x, 1.0, z)

    # Back face
    glVertex3f(-x, 0, -z)
    glVertex3f(x, 0, -z)
    glVertex3f(x, 1.0, -z)
    glVertex3f(-x, 1.0, -z)

    # Left face
    glVertex3f(-x, 0, -z)
    glVertex3f(-x, 0, z)
    glVertex3f(-x, 1.0, z)
    glVertex3f(-x, 1.0, -z)

    # Right face
    glVertex3f(x, 0, -z)
    glVertex3f(x, 0, z)
    glVertex3f(x, 1.0, z)
    glVertex3f(x, 1.0, -z)

    # Top face
    glVertex3f(-x, 1.0, -z)
    glVertex3f(x, 1.0, -z)
    glVertex3f(x, 1.0, z)
    glVertex3f(-x, 1.0, z)

    # Bottom face
    glVertex3f(-x, 0, -z)
    glVertex3f(x, 0, -z)
    glVertex3f(x, 0, z)
    glVertex3f(-x, 0, z)

    glEnd()
    glPopMatrix()

def rotate_lifeguard_and_wave():
    glPushMatrix()

    # Rotate the torso to simulate turning
    glRotatef(45, 0, 1, 0)  # Rotate 45 degrees on the Y-axis

    # Animate the waving arm
    wave_arm()

    glPopMatrix()

def wave_arm():
    # For simplicity, we'll animate the right arm by changing its position
    glPushMatrix()

    # Animate the right arm to "wave"
    glTranslatef(2.25, 3.0, 0.0)  # Translate to the right arm's position
    glRotatef(45, 1, 0, 0)  # Rotate the arm to wave (along the x-axis)

    # Draw the right arm as usual
    right_arm((1.0, 0.0, 0.0))  # Red color for the arm while waving

    glPopMatrix()