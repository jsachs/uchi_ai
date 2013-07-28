"""
Module to implement eigenvector decomposition using the power method
"""
from __future__ import division
from sys import argv
from math import sqrt

from matrix import Matrix, load_matrix, dot


def iterate(matrix, vector):
	"""Performs a single iteration in the power method eigendecomposition"""
	product = matrix * vector  # computes A*r
	norm = product.norm()
	new_vector = product/norm
	return new_vector

def power_method(k, epsilon, matrix):
	ev = [] # list of eigenvectors
	vals = [] # list of eigenvalues
	v = 0     # index for which eigenvector we're computing
	if k == 1: iterations = 0
	while v < k:
		r = Matrix(matrix.rows, 1)  # initialize default vector
		for i in range(r.rows):
			r.data[i][0] += 1

		# deflation for additional eigenvectors
		if v > 0:
			matrix = matrix - (ev[v-1]*ev[v-1].transpose())*vals[v-1] 
		# orthogonalization of random vector
		if v > 0:
			for l in range(v):
				r = r - ev[l] * dot(ev[l], r)

		counter = 0
		while True:
			if k == 1: iterations += 1
			r_prime = iterate(matrix, r)
			e_plus = r - r_prime
			e_minus = r + r_prime
			if e_plus.norm() < epsilon or e_minus.norm() < epsilon:
				ev.append(r)
				lmb = dot(matrix*r, r)/dot(r, r)
				vals.append(lmb)
				v += 1
				break
			r = r_prime
			"""
			This would occasionally make my code fail to converge,
			so you can comment it out if things hang.
			"""
			if counter%10 ==0:
				# orthogonalization of random vector
				if v > 0:
					for l in range(v):
						r = r - ev[l] * dot(ev[l], r)
			counter += 1

	if k == 1: print "Iterations:",iterations
	return ev, vals


def main():
	if len(argv) < 4:
		print "Usage: <num eigenvectors> <tolerance> <text file>"
		return
	data = load_matrix(argv[3])
	k = int(argv[1])
	epsilon = float(argv[2])
	rows = len(data)
	cols = len(data[0])
	A = Matrix(rows, cols, data)
	res, vals = power_method(k, epsilon, A)

	Vecs = Matrix(rows, k)
	for i in range(rows):
		for j in range(k):
			Vecs.data[i][j] = res[j].data[i][0]

	f1 = open('vecs.txt','w')
	f2 = open('vals.txt','w')

	# TODO fix formatting
	for i in range(rows):
		for j in range(k):
			f1.write(str(Vecs.data[i][j]) + ' ')
		f1.write('\n')

	for i in range(k):
		f2.write(str(vals[i]) + '\n')

	f1.close()
	f2.close()

if __name__ == '__main__':
	main()
