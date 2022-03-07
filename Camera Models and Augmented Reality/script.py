from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame, pygame.image
from pygame.locals import *
import pickle
width,height = 1000,747
def setup():
""" Setup window and pygame environment. """
pygame.init()
pygame.display.set_mode((width,height),OPENGL | DOUBLEBUF)
pygame.display.set_caption(’OpenGL AR demo’)
# load camera data
with open(’ar_camera.pkl’,’r’) as f:
K = pickle.load(f)
Rt = pickle.load(f)
setup()
draw_background(’book_perspective.bmp’)
set_projection_from_camera(K)
set_modelview_from_camera(Rt)
draw_teapot(0.02)
while True:
    event = pygame.event.poll()
    if event.type in (QUIT,KEYDOWN):
        break
    pygame.display.flip()
