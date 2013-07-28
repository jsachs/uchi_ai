"""
Module implementing the Linear Perceptron
"""
from __future__ import division

class LinearPerceptron(object):
	"""Class for the linear perceptron"""
	def __init__(self):
		self.w = [0] * 784  # Total vector size of our numbers

	def predict(self, x):
		"""Perceptron prediction function"""
		y = dot(self.w, x)
		if y >= 0:
			return 1
		else:
			return -1

	def train_online(self, data, labels):
		"""Trains the perceptron in online mode"""
		f = open('linear_online.txt','w')
		right = 0
		wrong = 0
		ex = 0
		for x, l in zip(data, labels):
			y_bar = self.predict(x)
			if y_bar == -1 and l[0] == 1:
				wrong += 1
				self.w = vec_sum(self.w, x)
			elif y_bar == 1 and l[0] == -1:
				wrong += 1
				self.w = vec_dif(self.w, x)
			else:
				right += 1
			ex += 1
			f.write(str(ex) + ' ' + str(wrong) + '\n')
		return right, wrong, wrong/len(data)

	def train_batch(self, data, labels):
		"""Trains the perceptron in batch mode"""
		done = False
		iteration = 0
		error = 0
		while not done:
			error = 0
			for x, l in zip(data, labels):
				y_bar = self.predict(x)
				if y_bar == -1 and l[0] == 1:
					error += 1
					self.w = vec_sum(self.w, x)
				if y_bar == 1 and l[0] == -1:
					error += 1
					self.w = vec_dif(self.w, x)
			iteration += 1
			if error == 0 or iteration > 100:
				done = True
		return iteration, error/len(data)

	def label_test(self, data):
		"""Produces predicted labels on test data"""
		f = open('test200.label.35.linear','w')
		for x in data:
			y_bar = self.predict(x)
			f.write(str(y_bar) + '\n')


def dot(v1, v2):
	"""Computes the dot product of two vectors"""
	if len(v1) != len(v2):
		return 0
	ret = sum([x1 * x2 for x1, x2 in zip(v1, v2)])
	return ret

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


