from OpenGL.GLUT import *
glutSolidTeapot(size)

def draw_teapot(size):
""" Draw a red teapot at the origin. """
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glClear(GL_DEPTH_BUFFER_BIT)
    # draw red teapot
    glMaterialfv(GL_FRONT,GL_AMBIENT,[0,0,0,0])
    glMaterialfv(GL_FRONT,GL_DIFFUSE,[0.5,0.0,0.0,0.0])
    glMaterialfv(GL_FRONT,GL_SPECULAR,[0.7,0.6,0.6,0.0])
    glMaterialf(GL_FRONT,GL_SHININESS,0.25*128.0)
    glutSolidTeapot(size)
