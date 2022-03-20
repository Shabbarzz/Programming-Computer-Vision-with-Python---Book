def triangulate_point(x1,x2,P1,P2):
""" Point pair triangulation from
least squares solution. """
    M = zeros((6,6))
    M[:3,:4] = P1
    M[3:,:4] = P2
    M[:3,4] = -x1
    M[3:,5] = -x2
    U,S,V = linalg.svd(M)
    X = V[-1,:4]
    return X / X[3]



def triangulate(x1,x2,P1,P2):
""" Two-view triangulation of points in
x1
,x2 (3*n homog. coordinates). """
    n = x1.shape[1]
    if x2.shape[1] != n:
    raise ValueError("Number of points don’t match.")
    X = [ triangulate_point(x1[:,i],x2[:,i],P1,P2) for i in range(n)]
    return array(X).T
