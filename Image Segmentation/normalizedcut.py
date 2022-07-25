def ncut_graph_matrix(im,sigma_d=1e2,sigma_g=1e-2):
""" Create matrix for normalized cut. The parameters are
the weights for pixel distance and pixel similarity. """
    m,n = im.shape[:2]
    N = m*n

# normalize and create feature vector of RGB or grayscale
if len(im.shape)==3:
    for i in range(3):
      im[:,:,i] = im[:,:,i] / im[:,:,i].max()
    vim = im.reshape((-1,3))
else:
    im = im / im.max()
    vim = im.flatten()

# x,y coordinates for distance computation
xx,yy = meshgrid(range(n),range(m))
x,y = xx.flatten(),yy.flatten()

# create matrix with edge weights
W = zeros((N,N),’f’)
for i in range(N):
    for j in range(i,N):
      d = (x[i]-x[j])**2 + (y[i]-y[j])**2
      W[i,j] = W[j,i] = exp(-1.0*sum((vim[i]-vim[j])**2)/sigma_g) * exp(-d/sigma_d)
return W

