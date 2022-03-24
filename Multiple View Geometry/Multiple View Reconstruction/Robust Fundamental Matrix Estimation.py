class RansacModel(object):
""" Class for fundmental matrix fit with ransac.py from
http://www.scipy.org/Cookbook/RANSAC"""
def __init__(self,debug=False):
   self.debug = debug

def fit(self,data):
    """ Estimate fundamental matrix using eight
    selected correspondences. """
    # transpose and split data into the two point sets
    data = data.T
    x1 = data[:3,:8]
    x2 = data[3:,:8]

    # estimate fundamental matrix and return
    F = compute_fundamental_normalized(x1,x2)
    return F

def get_error(self,data,F):
    """ Compute x^T F x for all correspondences,
    return error for each transformed point. """
    # transpose and split data into the two point
    data = data.T
    x1 = data[:3]
    x2 = data[3:]
    # Sampson distance as error measure
    Fx1 = dot(F,x1)
    Fx2 = dot(F,x2)
    denom = Fx1[0]**2 + Fx1[1]**2 + Fx2[0]**2 + Fx2[1]**2
    err = ( diag(dot(x1.T,dot(F,x2))) )**2 / denom
    # return error per point
    return err
