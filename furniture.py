import pygame
import OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pywavefront

scene = pywavefront.Wavefront('models/couch.obj', collect_faces=True)

scene_box = (scene.vertices[0], scene.vertices[0])
for vertex in scene.vertices:
    min_v = [min(scene_box[0][i], vertex[i]) for i in range(3)]
    max_v = [max(scene_box[1][i], vertex[i]) for i in range(3)]
    scene_box = (min_v, max_v)

scene_size     = [scene_box[1][i]-scene_box[0][i] for i in range(3)]
max_scene_size = max(scene_size)
scaled_size    = 5
scene_scale    = [scaled_size/max_scene_size for i in range(3)]
scene_trans    = [-(scene_box[1][i]+scene_box[0][i])/2 for i in range(3)]
                  
def draw_couch(x, y, z):
    glPushMatrix()
    
    glTranslatef(x,y,z)
    glColor(0.478, 0.373, 0.184)
    res = []
    for val in scene_scale:
        res.append(val * 1)
    glScalef(*res)
    glRotatef(-90, 0, 1, 0)
    for mesh in scene.mesh_list:
        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*scene.vertices[vertex_i])
        glEnd()
    glPopMatrix()

def draw_table(x, y, z):
    stand(x, y, z)
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor(.831, .718, 0.494)
    table()
    glPopMatrix()

def table():
    glBegin(GL_POLYGON)
    glVertex3f(1, 2, 3)
    glVertex3f(1, 2, 0)
    glVertex3f(3, 2, 0)
    glVertex3f(3, 2, 3)
    glEnd()

def stand(x, y, z):
    quad = gluNewQuadric()                    
    gluQuadricNormals(quad, GLU_SMOOTH)  
    glPushMatrix()  
    glColor(.831, .718, 0.494)
    glTranslatef(x+2, y+2, z+1)
    glRotatef(90, 1.0, 0.0, 0.0)
    gluCylinder(quad, .25, .25, 2, 10, 10)
    glPopMatrix()