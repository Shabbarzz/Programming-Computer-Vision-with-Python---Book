from itertools import combinations
class ClusterNode(object):
   def __init__(self,vec,left,right,distance=0.0,count=1):
    self.left = left
    self.right = right
    self.vec = vec
    self.distance = distance
    self.count = count # only used for weighted average
   def extract_clusters(self,dist):
""" Extract list of sub-tree clusters from
hcluster tree with distance<dist. """
    if self.distance < dist:
       return [self]
    return self.left.extract_clusters(dist) + self.right.extract_clusters(dist

def get_cluster_elements(self):
""" Return ids for elements in a cluster sub-tree. """
    return self.left.get_cluster_elements() + self.right.get_cluster_elements()

def get_height(self):
""" Return the height of a node,
height is sum of each branch. """
   return self.left.get_height() + self.right.get_height()

def get_depth(self):
""" Return the depth of a node, depth is
max of each child plus own distance. """
   return max(self.left.get_depth(), self.right.get_depth()) + self.distance


class ClusterLeafNode(object):
    def __init__(self,vec,id):
        self.vec = vec
        self.id = id
    def extract_clusters(self,dist):
        return [self]
    def get_cluster_elements(self):
        return [self.id]
    def get_height(self):
        return 1
    def get_depth(self):
        return 0

def L2dist(v1,v2):
    return sqrt(sum((v1-v2)**2))
def L1dist(v1,v2):
    return sum(abs(v1-v2))
def hcluster(features,distfcn=L2dist):
""" Cluster the rows of features using
hierarchical clustering. """
# cache of distance calculations
    distances = {}



# initialize with each row as a cluster
node = [ClusterLeafNode(array(f),id=i) for i,f in enumerate(features)]
while len(node)>1:
 closest = float(’Inf’)
# loop through every pair looking for the smallest distance
 for ni,nj in combinations(node,2):
    if (ni,nj) not in distances:
        distances[ni,nj] = distfcn(ni.vec,nj.vec)
    d = distances[ni,nj]
    if d<closest:
        closest = d
        lowestpair = (ni,nj)
    ni,nj = lowestpair
    # average the two clusters
    new_vec = (ni.vec + nj.vec) / 2.0
    # create new node
    new_node = ClusterNode(new_vec,left=ni,right=nj,distance=closest)
    node.remove(ni)
    node.remove(nj)
    node.append(new_node)
return node[0]
