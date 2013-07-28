"""
Module to test SVD with missing entries
"""
from __future__ import division
from sys import argv
from math import sqrt
from random import random, uniform

from matrix import Matrix, load_matrix, dot
from svdP import svd, frob_norm


def rand_mat_30():
	"""Returns a 30x30 random matrix"""
	A = Matrix(30, 30)
	left = rand_unit_vec()
	right = rand_unit_vec()

	for i in range(30):
		A.data[i][0] = left[i]
	for i in range(30):
		A.data[i][29] = right[i]
	for i in range(30):
		for j in range(1,29):
			A.data[i][j] = uniform(0.0,1.0)
	return A

def missing_entries(matrix, p):
	"""Takes a matrix and returns a version with randomly missing entries"""
	A_bar = matrix
	def delete():
		return False if random() < p else True
	for i in range(A_bar.rows):
		for j in range(A_bar.cols):
			if delete():
				A_bar.data[i][j] = 0
	return A_bar

def rand_unit_vec():
	"""Returns a list representing a vector from the unit sphere on R^30"""
	vec = Matrix(30,1)
	for i in range(30):
		vec.data[i][0] = uniform(0.0,1.0)
	vec = vec.normalize()
	ret = []
	for i in range(30):
		ret.append(vec.data[i][0])
	return ret


def main():
	if len(argv) < 3:
		print "Usage: <num eigenvectors> <probability>"
		return
	k = int(argv[1])
	p = float(argv[2])

	A = rand_mat_30()
	A_bar = missing_entries(A, p)

	U, S, V = svd(k, 0.0001, A_bar)
	print "Frobenius norm:", frob_norm(A, U, S, V)

if __name__ == '__main__':
	main()


