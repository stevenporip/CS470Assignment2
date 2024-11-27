from OpenGL.GL import *
import pygame
from pygame.locals import *
from OpenGL.GLU import *
# Variables to track the opening / closing of the door
front_door_angle = 0
door_opening_speed = 1
front_door_open = False
front_door_close = True
garage_down = True
garage_up = False
garage_move = 0

def draw_house(x, y, z, color, garage):
    glPushMatrix()
    glTranslatef(x, y, z)
    front(color)
    back(color)
    floor()
    if garage is True:
        side_right(color)
    elif garage is False:
        garage_side(color)
        garage_door()
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

def garage_side(color):
    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(1, 0, 0)
    glVertex3f(1, 0, 2)
    glVertex3f(1, 10, 2)
    glVertex3f(1, 10, 0)
    glEnd()

    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(1, 4, 2)
    glVertex3f(1, 4, 8)
    glVertex3f(1, 10, 8)
    glVertex3f(1, 10, 2)
    glEnd()

    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3f(1, 0, 8)
    glVertex3f(1, 0, 10)
    glVertex3f(1, 10, 10)
    glVertex3f(1, 10, 8)
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

def floor():
    glColor(.443, .541, .949)
    glBegin(GL_POLYGON)
    glVertex3f(1, 0.25, 10)
    glVertex3f(1, 0.25, 0)
    glVertex3f(15, 0.25, 0)
    glVertex3f(15, 0.25, 10)
    glEnd()

def front_door():
    glPushMatrix()
    glTranslatef(6, 0 , 10)
    glRotatef(front_door_angle, 0, 1, 0)
    glTranslatef(-6,0,-10)
    glColor3f(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex3f(6, 0.0, 10)
    glVertex3f(9, 0.0, 10)
    glVertex3f(9, 4.5, 10)
    glVertex3f(6, 4.5, 10)
    glEnd()
    glPopMatrix()

def back_door():
    glColor3f(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex3f(6, 0.0, 0)
    glVertex3f(9, 0.0, 0)
    glVertex3f(9, 4.5, 0)
    glVertex3f(6, 4.5, 0)
    glEnd()

def garage_door():
    glPushMatrix()
    glTranslatef(0, garage_move, 0)
    glColor3f(0.569, 0.549, 0.518)
    glBegin(GL_POLYGON)
    glVertex3f(1, 0, 2)
    glVertex3f(1, 0, 8)
    glVertex3f(1, 4, 8)
    glVertex3f(1, 4, 2)
    glEnd()
    glPopMatrix()

# Function to handle opening of doors
def handle_door_opening():
    global front_door_angle, front_door_open, front_door_close, garage_up, garage_down, garage_move

    # O to open door, P to close door
    keys = pygame.key.get_pressed()
    if keys[pygame.K_o]:  # Open door
        front_door_open = True
        front_door_close = False
    elif keys[pygame.K_p]:  # Close door
        front_door_open = False
        front_door_close = True
    elif keys[pygame.K_g]:
        garage_up = True
        garage_down = False
    elif keys[pygame.K_d]:
        garage_up = False
        garage_down = True

    if front_door_open and front_door_angle < 90:
        front_door_angle += door_opening_speed
    elif front_door_close and front_door_angle > 0:
        front_door_angle -= door_opening_speed
    elif garage_up and garage_move < 5:
        garage_move += door_opening_speed
    elif garage_down and garage_move > 0:
        garage_move -= door_opening_speed