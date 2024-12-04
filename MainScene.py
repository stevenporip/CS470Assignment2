import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from background import *
from objects import *
from house_reg import *
from car import *
from buildings import *
from water_tower import *
from boardwalk import *
from lifeguard_chair import *
from boat import *
from furniture import *
from mountain import *
from lifeguard import*

# Define camera positions and angles
camera_pos = [-42, -5, 1] # Starting Camera position
camera_rot = [0, -35] # for rotation

# Car Position
car_pos = [-10, 1.1, 28] # Starting Position for Car

# Boat Position
boat_pos = [10,0,145] #Start position for boat

def opengl():
    glClearColor(0.5, 0.8, 1, 1)  # Set sky color
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)         
    glEnable(GL_LIGHT0)            
    glEnable(GL_COLOR_MATERIAL)    
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800 / 600, 0.1, 300.0)
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
    camera_speed = 1.0
    rotational_speed = 1.0

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

    # Car Movement ( C to go forward (z axis), V to go backwards (x axis) )
    car_speed = 0.2
    if keys[K_c]: car_pos[0] -= car_speed  # Move car forward along z-axis
    if keys[K_v]: car_pos[0] += car_speed  # Move car back along z-axis

    # Boat Movement ( F to go forward, G to go backwards)
    boat_speed = 0.1
    if keys[K_f]: boat_pos[0] -= boat_speed  # Move boat forward
    if keys[K_g]: boat_pos[0] += boat_speed  # Move boat backwards

    # TESTING
    print(f"Camera Position: x={camera_pos[0]}, y={camera_pos[1]}, z={camera_pos[2]}")
    # print(f"Car Position: x={car_pos[0]}, y={car_pos[1]}, z={car_pos[2]}")

def lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 100.0, 0.0, 1.0])  # Light positioned above the scene
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_day)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_day)

# Define Lighting
is_daytime = True  # Start with daytime

ambient_day = [1.2, 1.2, 1.2, 1.0] 
diffuse_day = [1.2, 1.2, 1.2, 1.0]
 
ambient_night = [0.1, 0.1, 0.2, 1.0] 
diffuse_night = [0.2, 0.2, 0.4, 1.0]  

def update_lighting():
    global is_daytime  
    keys = pygame.key.get_pressed()
    
    if keys[K_m]:  # Daytime key
        is_daytime = True
        glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_day)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_day)
        glDisable(GL_LIGHT1)  # Turn off interior lights
        glClearColor(0.5, 0.8, 1, 1) 
        
    elif keys[K_n]:  # Nighttime key
        is_daytime = False
        glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_night)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_night)
        glEnable(GL_LIGHT1)  # Turn on interior lights
        glLightfv(GL_LIGHT1, GL_DIFFUSE, [1.0, 0.8, 0.6, 1.0])  
        glLightfv(GL_LIGHT1, GL_SPECULAR, [1.0, 0.8, 0.6, 1.0]) 
        glClearColor(0.0, 0.0, 0.0, 1)


def main():
    # Initialize Game
    pygame.init()
    # Set Display window size
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)
    opengl() # Set up OpenGl

    lighting()
    
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
        
        update_lighting()

        # Handle Opening of Door input
        handle_door_opening()

        # Draw Scenes / Objects
        glColor3f(1.0, 1.0, 1.0)
        
        draw_ground(texture)
        draw_water(texture2)
        draw_sand(texture3)
        
        draw_street()
        draw_perpendicular_street()
        
        draw_traffic_light(0, 0,-35, 2)
        
        streetlight_positions = [(-50, 0, -32), (-25, 0, -32), (25, 0, -32), (50, 0, -32)]
        for i, pos in enumerate(streetlight_positions):
            draw_streetlight(pos[0], pos[1], pos[2], GL_LIGHT0 + i, is_daytime)
        
        draw_tree(-85,0,-20)
        draw_tree(-70,0,-23)
        draw_tree(-55,0,-17)
        draw_tree(-23,0,-48)
        draw_tree(-30,0,-48)
        draw_tree(-60,0,-48)
        draw_tree(-70,0,-59)
        draw_tree(-74,0,-48)
        draw_tree(-78,0,-59)
        draw_tree(-82,0,-48)
        draw_tree(-88,0,-52)
        draw_tree(-88,0,-64)
        draw_tree(-80,0,-70)
        
        draw_house(-25, 0, -65, (0.251, 0.922, 0.663), True)
        draw_couch(-17, 1.5 , -62.5)
        draw_table(-19, 0, -60)
        
        draw_house(-45, 0, -65, (0.444, 0.222, 0.563), False)
        draw_couch(-37, 1.5 , -62.5)
        draw_table(-39, 0, -60)
        
        draw_house(10, 0, -65, (0.949, 0.443, 0.627), True)
        draw_couch(19, 1.5 , -62.5)
        draw_table(17, 0, -60)
        
        draw_building(45, 0, -65, (1, 0, 0))
        
        draw_car(car_pos[0], car_pos[1], car_pos[2])
        
        draw_palmtree(-115,0,105)
        draw_palmtree(-85,0,105)
        draw_palmtree(-50, 0, 105)
        draw_palmtree(-25,0,105)
        draw_palmtree(0,0,105)
        draw_palmtree(25,0,105)
        
        draw_tower(20, 7, 65)
        
        draw_boardwalk(-95, 2, 155)
        
        draw_boat(boat_pos[0], boat_pos[1], boat_pos[2])

        draw_lifeguard(5, 0, 110, (255, 0, 0), (237, 187, 153))

        draw_lifeguardchair(15,0,110)
        draw_lifeguardchair(-10,0,110)
        draw_lifeguardchair(-36,0,110)
        draw_lifeguardchair(-66,0,110)
        draw_lifeguardchair(-106,0,110)
        
        draw_mountain(100, 90, [35, 0, -200])
        draw_mountain(150, 90, [-65, 0, -200])
        draw_mountain(70,120, [-105,0,-150])
        draw_mountain(70,120, [-175,0,-65])
        draw_mountain(50,40, [-135,0,-110])
        draw_mountain(40,20,[-95,0,-110])
        draw_mountain(75,30,[-70,0,-110])
        draw_mountain(60,60,[-30,0,-110])
        draw_mountain(75,40, [45,0,-110])
        draw_mountain(60,50,[75,0,-75])
        draw_mountain(30,25,[50,0,-35])
        draw_mountain(50,40, [20,0,-110])
        draw_mountain(50,90, [-15,0,-150])
        draw_mountain(50,60, [75,0,-150])
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()