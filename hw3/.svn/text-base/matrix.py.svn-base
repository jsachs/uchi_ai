"""
Module to implement matrix operations
"""
from __future__ import division
from sys import argv
from math import sqrt

def load_matrix(fname):
	"""Loads a matrix as data from a text file"""
	lines = open(fname,'r').readlines()
	ret = []
	for line in lines:
		line = line[:-1].split()
		line = [int(i) for i in line]
		ret.append(line)
	return ret
	# TODO deal with trailing characters

class Matrix(object):
	"""Matrix class for eigendecomposition"""
	def __init__(self, rows, cols, data = None):
		self.rows = rows
		self.cols = cols
		if data:
			self.data = data
		else:
			# default value of 0
			self.data = []
			for i in range(self.rows):
				temp = []
				for j in range(self.cols):
					temp.append(0)
				self.data.append(temp)

	def __add__(self, other):
		"""Operator overloading for matrix addition"""
		data = []
		for i in range(self.rows):
			line = []
			for j in range(self.cols):
				line.append(self.data[i][j] + other.data[i][j])
			data.append(line)
		return Matrix(self.rows, self.cols, data)

	def __sub__(self, other):
		"""Operator overloading for matrix subtraction"""
		data = []
		for i in range(self.rows):
			line = []
			for j in range(self.cols):
				line.append(self.data[i][j] - other.data[i][j])
			data.append(line)
		return Matrix(self.rows, self.cols, data)

	def __mul__(self, other):
		"""Operator overloading for matrix multiplication"""
		if isinstance(other, self.__class__):
			C = Matrix(self.rows, other.cols)
			for i in range(self.rows):
				for j in range(other.cols):
					for k in range(self.cols):
						C.data[i][j] += self.data[i][k] * other.data[k][j]
			return C
		elif isinstance(other, int):
			# scalar multiplication
			B = Matrix(self.rows, self.cols)
			for i in range(self.rows):
				for j in range(self.cols):
					B.data[i][j] += self.data[i][j] * other
			return B
		elif isinstance(other, float):
			# scalar multiplication
			B = Matrix(self.rows, self.cols)
			for i in range(self.rows):
				for j in range(self.cols):
					B.data[i][j] += self.data[i][j] * other
			return B

	def __truediv__(self, scalar):
		"""Operator overloading for scalar matrix division"""
		B = Matrix(self.rows, self.cols)
		for i in range(self.rows):
			for j in range(self.cols):
				B.data[i][j] += self.data[i][j]/scalar
		return B

	def norm(self):
		"""Calculates the length of a vector matrix"""
		if self.cols > 1:
			print "Error: norm requires column vector"
			return 0
		norm_squared = 0
		for i in range(self.rows):
			norm_squared += self.data[i][0] * self.data[i][0]
		return sqrt(norm_squared)

	def transpose(self):
		"""Returns the transpose of the matrix"""
		T = Matrix(self.cols, self.rows)
		for i in range(self.rows):
			for j in range(self.cols):
				T.data[j][i] = self.data[i][j]
		return T

	def normalize(self):
		"""Returns the normalized version of a column vector"""
		V = Matrix(self.rows, 1)
		norm = self.norm()
		for i in range(self.rows):
			V.data[i][0] = self.data[i][0] / norm
		return V

def dot(vec1, vec2):
	"""Computes the dot product of two column vectors"""
	sum = 0
	for i in range(vec1.rows):
		sum += vec1.data[i][0] * vec2.data[i][0]
	return sum




