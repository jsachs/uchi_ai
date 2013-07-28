"""
==================================================
Question 1: Output on an Iris subset
==================================================

Generates outputs for the different SVM classifiers
on the provided subset of the iris dataset.

"""
print __doc__

import numpy as np
import pylab as pl
from sklearn import svm, datasets

# load data from local files
fx = open('../data/iris_data.dat', 'r')
fy = open('../data/iris_labels.dat', 'r')
X = []
Y = []

lines = fx.readlines()
for line in lines:
    line = line.split()
    temp = []
    for num in line:
        temp.append(float(num[:7]))
    X.append(temp)

lines = fy.readlines()
for line in lines:
    line = line.split()
    num = float(line[0][:7])
    Y.append(num)

fx.close()
fy.close()

X = np.array(X)
Y = np.array(Y)

h = .02  # step size in the mesh

# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
C = 1.0  # SVM regularization parameter
svc = svm.SVC(kernel='linear', C=C).fit(X, Y)
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, Y)
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, Y)
lin_svc = svm.LinearSVC(C=C).fit(X, Y)

# create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# title for the plots
titles = ['SVC with linear kernel',
          'SVC with RBF kernel',
          'SVC with polynomial (degree 3) kernel',
          'LinearSVC (linear kernel)']


for i, clf in enumerate((svc, rbf_svc, poly_svc, lin_svc)):
    # Plot the decision boundary. For that, we will asign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    pl.subplot(2, 2, i + 1)
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    pl.contourf(xx, yy, Z, cmap=pl.cm.Paired)
    pl.axis('off')

    # Plot also the training points
    pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)

    pl.title(titles[i])

pl.show()

