def set_modelview_from_camera(Rt):
""" Set the model view matrix from camera pose. """
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
# rotate teapot 90 deg around x-axis so that z-axis is up
   Rx = array([[1,0,0],[0,0,-1],[0,1,0]])
# set rotation to best approximation
   R = Rt[:,:3]
   U,S,V = linalg.svd(R)
   R = dot(U,V)
   R[0,:] = -R[0,:] # change sign of x-axis
# set translation
   t = Rt[:,3]
# setup 4*4 model view matrix
   M = eye(4)
   M[:3,:3] = dot(R,Rx)
   M[:3,3] = t
# transpose and flatten to get column order
   M = M.T
   m = M.flatten()
# replace model view with the new matrix
   glLoadMatrixf(m)


