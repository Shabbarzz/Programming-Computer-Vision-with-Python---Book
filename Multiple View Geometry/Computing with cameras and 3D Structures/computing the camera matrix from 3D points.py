def compute_P(x,X):
""" Compute camera matrix from pairs of
2D-3D correspondences (in homog. coordinates). """
    n = x.shape[1]
    if X.shape[1] != n:
    raise ValueError("Number of points don’t match.")
    # create matrix for DLT solution
    M = zeros((3*n,12+n))
    for i in range(n):
        M[3*i,0:4] = X[:,i]
        M[3*i+1,4:8] = X[:,i]
        M[3*i+2,8:12] = X[:,i]
        M[3*i:3*i+3,i+12] = -x[:,i]
        U,S,V = linalg.svd(M)
    return V[-1,:12].reshape((3,4))


import sfm, camera
corr = corr[:,0] # view 1
ndx3D = where(corr>=0)[0] # missing values are -1
ndx2D = corr[ndx3D]
# select visible points and make homogeneous
x = points2D[0][:,ndx2D] # view 1
x = vstack( (x,ones(x.shape[1])) )
X = points3D[:,ndx3D]
X = vstack( (X,ones(X.shape[1])) )
# estimate P
Pest = camera.Camera(sfm.compute_P(x,X))
# compare!
print Pest.P / Pest.P[2,3]
print P[0].P / P[0].P[2,3]
xest = Pest.project(X)
# plotting
figure()
imshow(im1)
plot(x[0],x[1],’b.’)
plot(xest[0],xest[1],’r.’)
axis(’off’)
show()
