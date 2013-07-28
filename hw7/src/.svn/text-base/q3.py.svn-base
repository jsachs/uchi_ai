"""
==================================================
Question 3: Sample complexity and parameters
==================================================



"""
from __future__ import division
print __doc__

import numpy as np
import pylab as pl
from sklearn import svm, datasets

def test_loss(problem, kernel, kernel_parameter, alpha, gamma):
	# Parse out the data (all numpy arrays)
	data, labels, test_data, test_labels = problem

	if kernel == 'linear':
		svc = svm.SVC(kernel=kernel, C=gamma).fit(data, labels)
	elif kernel == 'rbf':
		svc = svm.SVC(kernel=kernel, gamma=kernel_parameter, C=gamma).fit(data, labels)
	elif kernel == 'poly':
		svc = svm.SVC(kernel=kernel, degree=kernel_parameter, C=gamma).fit(data, labels)
	else:
		pass

	# Compare predicted labels
	Z = svc.predict(test_data)
	right = 0
	wrong = 0
	for t, l in zip(Z, test_labels):
		if t == l:
			right += 1
		else:
			wrong += 1

	print "==========================="
	print "Kernel:", kernel
	print "Parameter:", kernel_parameter
	print "Alpha:", alpha
	print "Gamma:", gamma
	print "Accuracy:", right/(right+wrong)
	print "==========================="


def main():
	# Parameters to test
	alphas = [.01,.1,1,10,50,100]
	degrees = [1,2,3,4]
	gammas = [.1,.3,.5,.7,.9]
	margins = [.2,.4,.6,.8,1]
	kernels = ['linear','rbf','poly']

	# Read in all of the data
	f0d = open('../data/zeros-train.txt', 'r')
	f0t = open('../data/zeros-test.txt', 'r')
	f1d = open('../data/ones-train.txt', 'r')
	f1t = open('../data/ones-test.txt', 'r')
	f7d = open('../data/sevens-train.txt', 'r')
	f7t = open('../data/sevens-test.txt', 'r')
	zeros_train  = []
	ones_train   = []
	sevens_train = []
	zeros_test   = []
	ones_test    = []
	sevens_test  = []

	for f, X in zip([f0d, f1d, f7d], [zeros_train,ones_train,sevens_train]):
		lines = f.readlines()
		for line in lines:
			line = line.split()
			temp = []
			for num in line:
				temp.append(float(num[:7]))
			X.append(temp)

	for f, X in zip([f0t, f1t, f7t], [zeros_test,ones_test,sevens_test]):
		lines = f.readlines()
		for line in lines:
			line = line.split()
			temp = []
			for num in line:
				temp.append(float(num[:7]))
			X.append(temp)

	files = [f0d,f0t,f1d,f1t,f7d,f7t]
	for f in files:
		f.close()

	# Problem (a)
	print "===================================="
	print "===================================="
	print " PROBLEM A: 0's v. 1's"
	print "===================================="
	print "===================================="
	# Linear testing
	for alpha in alphas:
		for gamma in margins:
			testX = np.array(zeros_test + ones_test)
			testY = np.array(len(zeros_test)*[0] + len(ones_test)*[1])
			data_0 = int(round((alpha/100)*len(zeros_train)))
			data_1 = int(round((alpha/100)*len(ones_train)))
			trainX = np.array(zeros_train[:data_0] + ones_train[:data_1])
			trainY = np.array(len(zeros_train[:data_0])*[0] + len(ones_train[:data_1])*[1])
			prob = (trainX, trainY, testX, testY)
			test_loss(prob, 'linear', None, alpha, gamma)

	# Gaussian testing
	for alpha in alphas:
		for gamma in margins:
			for p in gammas:
				testX = np.array(zeros_test + ones_test)
				testY = np.array(len(zeros_test)*[0] + len(ones_test)*[1])
				data_0 = int(round((alpha/100)*len(zeros_train)))
				data_1 = int(round((alpha/100)*len(ones_train)))
				trainX = np.array(zeros_train[:data_0] + ones_train[:data_1])
				trainY = np.array(len(zeros_train[:data_0])*[0] + len(ones_train[:data_1])*[1])
				prob = (trainX, trainY, testX, testY)
				test_loss(prob, 'rbf', p, alpha, gamma)

	# Polynomial testing
	for alpha in alphas:
		for gamma in margins:
			for deg in degrees:
				testX = np.array(zeros_test + ones_test)
				testY = np.array(len(zeros_test)*[0] + len(ones_test)*[1])
				data_0 = int(round((alpha/100)*len(zeros_train)))
				data_1 = int(round((alpha/100)*len(ones_train)))
				trainX = np.array(zeros_train[:data_0] + ones_train[:data_1])
				trainY = np.array(len(zeros_train[:data_0])*[0] + len(ones_train[:data_1])*[1])
				prob = (trainX, trainY, testX, testY)
				test_loss(prob, 'poly', deg, alpha, gamma)

	# Problem (b)
	print "===================================="
	print "===================================="
	print " PROBLEM B: 1's v. 7's"
	print "===================================="
	print "===================================="
	# Linear testing
	for alpha in alphas:
		for gamma in margins:
			testX = np.array(ones_test + sevens_test)
			testY = np.array(len(ones_test)*[0] + len(sevens_test)*[1])
			data_0 = int(round((alpha/100)*len(ones_train)))
			data_1 = int(round((alpha/100)*len(sevens_train)))
			trainX = np.array(ones_train[:data_0] + sevens_train[:data_1])
			trainY = np.array(len(ones_train[:data_0])*[0] + len(sevens_train[:data_1])*[1])
			prob = (trainX, trainY, testX, testY)
			test_loss(prob, 'linear', None, alpha, gamma)

	# Gaussian testing
	for alpha in alphas:
		for gamma in margins:
			for p in gammas:
				testX = np.array(zeros_test + ones_test)
				testY = np.array(len(zeros_test)*[0] + len(ones_test)*[1])
				data_0 = int(round((alpha/100)*len(zeros_train)))
				data_1 = int(round((alpha/100)*len(ones_train)))
				trainX = np.array(zeros_train[:data_0] + ones_train[:data_1])
				trainY = np.array(len(zeros_train[:data_0])*[0] + len(ones_train[:data_1])*[1])
				prob = (trainX, trainY, testX, testY)
				test_loss(prob, 'rbf', p, alpha, gamma)

	# Polynomial testing
	for alpha in alphas:
		for gamma in margins:
			for deg in degrees:
				testX = np.array(zeros_test + ones_test)
				testY = np.array(len(zeros_test)*[0] + len(ones_test)*[1])
				data_0 = int(round((alpha/100)*len(zeros_train)))
				data_1 = int(round((alpha/100)*len(ones_train)))
				trainX = np.array(zeros_train[:data_0] + ones_train[:data_1])
				trainY = np.array(len(zeros_train[:data_0])*[0] + len(ones_train[:data_1])*[1])
				prob = (trainX, trainY, testX, testY)
				test_loss(prob, 'poly', deg, alpha, gamma)

if __name__ == '__main__':
	main()










