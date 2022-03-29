import imtools
import pickle
from scipy.cluster.vq import *
# get list of images
imlist = imtools.get_imlist(’selected_fontimages/’)
imnbr = len(imlist)
# load model file
with open(’a_pca_modes.pkl’,’rb’) as f:
immean = pickle.load(f)
V = pickle.load(f)
# create matrix to store all flattened images
immatrix = array([array(Image.open(im)).flatten()
for im in imlist],’f’)

# project on the 40 first PCs
immean = immean.flatten()
projected = array([dot(V[:40],immatrix[i]-immean) for i in range(imnbr)])
# k-means
projected = whiten(projected)
centroids,distortion = kmeans(projected,4)
code,distance = vq(projected,centroids)

# plot clusters
for k in range(4):
    ind = where(code==k)[0]
    figure()
    gray()
    for i in range(minimum(len(ind),40)):
        subplot(4,10,i+1)
        imshow(immatrix[ind[i]].reshape((25,25)))
        axis(’off’)
show()
