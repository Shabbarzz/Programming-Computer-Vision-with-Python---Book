from mpl_toolkits.mplot3d import axes3d
fig = figure()
ax = fig.gca(projection="3d")
# generate 3D sample data
X,Y,Z = axes3d.get_test_data(0.25)
# plot the points in 3D
ax.plot(X.flatten(),Y.flatten(),Z.flatten(),’o’)
show()

# plotting 3D points
from mpl_toolkits.mplot3d import axes3d
fig = figure()
ax = fig.gca(projection=’3d’)
ax.plot(points3D[0],points3D[1],points3D[2],’k.’)
