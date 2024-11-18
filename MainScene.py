import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from background import *
from objects import *
from house_reg import *
from car import *


# Define camera positions and angles
camera_pos = [0.0, -5, -20] # Starting Camera position
camera_rot = [0.0, 0.0] # for rotation

def opengl():
    glClearColor(0.5, 0.8, 1, 1)  # Set sky color
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800 / 600, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    update_camera()

def update_camera():
    glLoadIdentity()

    # Apply camera rotation
    glRotatef(camera_rot[0], 1, 0, 0)  # Pitch rotation
    glRotatef(camera_rot[1], 0, 1, 0)  # Yaw rotation

    # Apply camera translation after rotation
    glTranslatef(camera_pos[0], camera_pos[1], camera_pos[2])

def handle_camera_movement():
    keys = pygame.key.get_pressed()
    camera_speed = 0.1
    rotational_speed = 0.2

    # Camera Translating ( WASD Format ) 
    if keys[K_w]: camera_pos[2] += camera_speed # Move Camera Forward
    if keys[K_a]: camera_pos[0] += camera_speed # Move Camera Left
    if keys[K_d]: camera_pos[0] -= camera_speed # Move Camera Right
    if keys[K_s]: camera_pos[2] -= camera_speed

    # Camera Rotation ( UP DOWN LEFT RIGHT Arrows to rotate camera )
    if keys[K_DOWN]: camera_rot[0] += rotational_speed  # Rotate up
    if keys[K_UP]: camera_rot[0] -= rotational_speed  # Rotate down
    if keys[K_RIGHT]: camera_rot[1] += rotational_speed  # Rotate left
    if keys[K_LEFT]: camera_rot[1] -= rotational_speed  # Rotate right

    # Camera Vertical Movement ( Q to go up, E to go down)
    if keys[K_q]: camera_pos[1] += camera_speed
    if keys[K_e]: camera_pos[1] -= camera_speed

def main():
    # Initialize Game
    pygame.init()
    # Set Display window size
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)

    opengl() # Set up OpenGl

    # Load Textures
    texture = load_texture('assets/ground_texture.jpg') # Ground Texture
    texture2 = load_texture('assets/water_texture.jpg') # Water Texture
    texture3 = load_texture('assets/sand_texture.jpg') # Sand Texture

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Update Camera
        handle_camera_movement()
        update_camera()

        # Draw Scenes / Objects
        glColor3f(1.0, 1.0, 1.0)
        draw_ground(texture)
        draw_water(texture2)
        draw_sand(texture3)
        draw_street()
        draw_tree(0,0,0)
        draw_tree(10,0,10)
        draw_tree(-5,0,-5)
        draw_house(-25, 0, 0, (0.88, 0.77, 0.91))
        draw_house(-25, 0, 0, (0.75, 0.91, 0.91))
        draw_car(80,1.1,20)
        draw_palmtree(10,0,-10)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()