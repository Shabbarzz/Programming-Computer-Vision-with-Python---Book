def F_from_ransac(x1,x2,model,maxiter=5000,match_theshold=1e-6):
    """ Robust estimation of a fundamental matrix F from point
    correspondences using RANSAC (ransac.py from
    http://www.scipy.org/Cookbook/RANSAC).
    input: x1,x2 (3*n arrays) points in hom. coordinates. """
    import ransac
    data = vstack((x1,x2))
    # compute F and return with inlier index
    F,ransac_data = ransac.ransac(data.T,model,8,maxiter,match_theshold,20,return_all=True)
    return F, ransac_data[’inliers’]
