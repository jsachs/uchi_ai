"""
Module implementing the Kernel Perceptron
"""
from __future__ import division
from math import exp, sqrt

class KernelPerceptron(object):
	"""Class for the linear perceptron"""
	def __init__(self, data, labels):
		self.c = [0] * len(data)  # List of constants for kernel calculations
		self.data = data
		self.labels = labels

	def kernel(self, t, K):
		"""Kernel function on a GRAM matrix"""
		y = sum([self.c[i] * K[i][t] for i in range(t)])
		if y >= 0:
			return 1
		else:
			return -1

	def kernel_batch(self, t, K):
		"""Kernel function on a GRAM matrix, inclusive of t"""
		y = sum([self.c[i] * K[i][t] for i in range(len(K))])
		if y >= 0:
			return 1
		else:
			return -1

	def train_online(self, sigma):
		"""Trains the perceptron in online mode"""
		f = open('kernel_online.txt','w')
		right = 0
		wrong = 0
		t = 0

		# GRAM matrix
		K = []
		for i in range(len(self.data)):
			new = []
			for j in range(len(self.data)):
				new.append(gauss(self.data[i], self.data[j], sigma))
			K.append(new)

		for x, l in zip(self.data, self.labels):
			y_bar = self.kernel(t, K)
			self.c[t] = 0
			if y_bar == -1 and l[0] == 1:
				wrong += 1
				self.c[t] = 1
			elif y_bar == 1 and l[0] == -1:
				wrong += 1
				self.c[t] = -1
			else:
				right += 1
			t += 1
			f.write(str(t) + ' ' + str(wrong) + '\n')
		return right, wrong, wrong/len(self.data)

	def train_batch(self, sigma):
		"""Train the perceptron in batch mode"""
		done = False
		iteration = 0

		# GRAM matrix
		K = []
		for i in range(len(self.data)):
			new = []
			for j in range(len(self.data)):
				new.append(gauss(self.data[i], self.data[j], sigma))
			K.append(new)

		while not done:
			error = 0
			t = 0
			for x, l in zip(self.data, self.labels):
				if iteration == 0:
					y_bar = self.kernel(t, K)
					self.c[t] = 0
				else:
					y_bar = self.kernel_batch(t, K)
				if y_bar == -1 and l[0] == 1:
					error += 1
					self.c[t] += 1
				elif y_bar == 1 and l[0] == -1:
					error += 1
					self.c[t] += -1
				t += 1
			iteration += 1
			if error == 0 or iteration > 100:
				done = True
		return iteration, error/len(self.data)

	def label_test(self, data, sigma):
		"""Produces predicted labels on test data"""
		f = open('test200.label.35.kernel','w')

		K = []
		for i in range(len(data)):
			new = []
			for j in range(len(data)):
				new.append(gauss(data[i], data[j], sigma))
			K.append(new)

		for t in range(len(data)):
			y_bar = self.kernel_batch(t, K)
			f.write(str(y_bar) + '\n')


def dot(v1, v2):
	"""Computes the dot product of two vectors"""
	if len(v1) != len(v2):
		return 0
	ret = sum([x1 * x2 for x1, x2 in zip(v1, v2)])
	return ret

def norm(v1, v2):
	"""Computes the Euclidean norm of the difference of two vectors"""
	v = vec_dif(v1, v2)
	val = sum([x**2 for x in v])
	return sqrt(val)

def gauss(v1, v2, sigma):
	"""Computes the gaussian of two vectors"""
	if len(v1) != len(v2):
		return 0
	num = -1 * (norm(v1, v2)**2)
	denom = 2*(sigma**2)
	return exp(num/denom)

def vec_sum(v1, v2):
	"""Computes the vector sum of two vectors"""
	if len(v1) != len(v2):
		return 0
	ret = [x1 + x2 for x1, x2 in zip(v1, v2)]
	return ret

def vec_dif(v1, v2):
	"""Computes the vector difference of two vectors"""
	if len(v1) != len(v2):
		return 0
	ret = [x1 - x2 for x1, x2 in zip(v1, v2)]
	return ret
