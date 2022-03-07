def set_projection_from_camera(K):
    # Set view from a camera calibration matrix. """
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    fx = K[0, 0]
    fy = K[1, 1]


    fovy = 2 * arctan(0.5 * height / fy) * 180 / pi
    aspect = (width * fy) / (height * fx)
# define the near and far clipping planes
    near = 0.1
    far = 100.0
# set perspective
    gluPerspective(fovy, aspect, near, far)
    glViewport(0, 0, width, height)
