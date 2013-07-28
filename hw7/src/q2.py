"""
==================================================
Question 2: Datasets satisfying constraints
==================================================

Generates outputs for the different datasets meeting the
requirements in the project specification.

"""
print __doc__

import numpy as np
import pylab as pl
from sklearn import svm, datasets

def part1():
    """
    Linear SVM with two support vectors
    """
    print part1.__doc__

    X = [[4,3],[4.5,2],[4.5,4],[3.5,3],[3,2],[3,4]]
    Y = [1,1,1,2,2,2]

    X = np.array(X)
    Y = np.array(Y)

    h = .02  # step size in the mesh

    # we create an instance of SVM and fit out data. We do not scale our
    # data since we want to plot the support vectors
    C = 1.0  # SVM regularization parameter
    svc = svm.SVC(kernel='linear', C=C).fit(X, Y)

    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    # title for the plots
    titles = ['SVC with linear kernel']

    # Plot the decision boundary. For that, we will asign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    pl.contourf(xx, yy, Z, cmap=pl.cm.Paired)
    pl.axis('off')

    # Plot also the training points
    pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)

    pl.title(titles[0])
    pl.show()



def part2():
    """
    Linear SVM with four support vectors
    """
    print part2.__doc__

    X = [[4,3],[4,3.5],[4.5,2],[4.5,4],
         [3.5,3],[3.5,3.5],[3,2],[3,4]]
    Y = [1,1,1,1,2,2,2,2]

    X = np.array(X)
    Y = np.array(Y)

    h = .02  # step size in the mesh

    # we create an instance of SVM and fit out data. We do not scale our
    # data since we want to plot the support vectors
    C = 1.0  # SVM regularization parameter
    svc = svm.SVC(kernel='linear', C=C).fit(X, Y)

    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    # title for the plots
    titles = ['SVC with linear kernel']

    # Plot the decision boundary. For that, we will asign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    pl.contourf(xx, yy, Z, cmap=pl.cm.Paired)
    pl.axis('off')

    # Plot also the training points
    pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)

    pl.title(titles[0])
    pl.show()

def part3():
    """
    Separable by 3rd order poly, not linear
    """
    print part3.__doc__

    X = [[2,2],[2,2.5],[2.5,2.5],[2.5,2],[3,3],
         [1,1],[1.5,3],[1,1.5],[3,1],[1.5,1]]
    Y = [0,0,0,0,0,1,1,1,1,1]

    X = np.array(X)
    Y = np.array(Y)

    h = .02  # step size in the mesh

    # we create an instance of SVM and fit out data. We do not scale our
    # data since we want to plot the support vectors
    C = 1.0  # SVM regularization parameter
    svc = svm.SVC(kernel='linear', C=C).fit(X, Y)
    poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, Y)

    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    # title for the plots
    titles = ['SVC with linear kernel',
              'SVC with polynomial (degree 3) kernel']

    for i, clf in enumerate((svc, poly_svc)):
        # Plot the decision boundary. For that, we will asign a color to each
        # point in the mesh [x_min, m_max]x[y_min, y_max].
        pl.subplot(2, 1, i + 1)
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        pl.contourf(xx, yy, Z, cmap=pl.cm.Paired)
        pl.axis('off')

        # Plot also the training points
        pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)

        pl.title(titles[i])

    pl.show()

def part4():
    """
    Separable by Gaussian, not 3rd order poly
    """
    print part4.__doc__

    X = [[2,2],[2,2.5],[2.5,2.5],[2.5,2],
         [1,1],[1,3],[3,3],[3,1]]
    Y = [0,0,0,0,1,1,1,1]

    X = np.array(X)
    Y = np.array(Y)

    h = .02  # step size in the mesh

    # we create an instance of SVM and fit out data. We do not scale our
    # data since we want to plot the support vectors
    C = 1.0  # SVM regularization parameter
    rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, Y)
    poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, Y)

    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    # title for the plots
    titles = ['SVC with RBF kernel',
              'SVC with polynomial (degree 3) kernel']

    for i, clf in enumerate((rbf_svc, poly_svc)):
        # Plot the decision boundary. For that, we will asign a color to each
        # point in the mesh [x_min, m_max]x[y_min, y_max].
        pl.subplot(2, 1, i + 1)
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        pl.contourf(xx, yy, Z, cmap=pl.cm.Paired)
        pl.axis('off')

        # Plot also the training points
        pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)

        pl.title(titles[i])

    pl.show()


part1()
part2()
part3()
part4()



