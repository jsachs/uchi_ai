"""
Module to compute the SVD of a matrix
"""
from __future__ import division
from sys import argv
from math import sqrt

from matrix import Matrix, load_matrix, dot
from eigP import iterate, power_method


def svd(k, epsilon, matrix):
	# Get the matrix U
	W = matrix * matrix.transpose()
	U_vecs, U_vals = power_method(k, epsilon, W)
	U = Matrix(W.rows, k)
	for i in range(U.rows):
		for j in range(U.cols):
			U.data[i][j] = U_vecs[j].data[i][0]

	# Get the matrix V
	W = matrix.transpose() * matrix
	V_vecs, V_vals = power_method(k, epsilon, W)
	V = Matrix(W.rows, k)
	for i in range(V.rows):
		for j in range(V.cols):
			V.data[i][j] = V_vecs[j].data[i][0]

	# Get the values for S
	S_vals = [sqrt(abs(V_vals[i])) for i in range(k)]

	# Format and return the results
	return U, S_vals, V

def frob_norm(A, U, S_vals, V):
	S = Matrix(len(S_vals),len(S_vals))
	for i in range(S.rows):
		for j in range(S.cols):
			if i == j:
				S.data[i][j] = S_vals[i]
	Vt = V.transpose()
	Recon = U*S*Vt
	total = 0

	for i in range(A.rows):
		for j in range(A.cols):
			total += (A.data[i][j] - Recon.data[i][j])**2

	ret = sqrt(total)
	return ret


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
	U, S, V = svd(k, epsilon, A)

	f1 = open('U.txt','w')
	f2 = open('V.txt','w')
	f3 = open('S.txt','w')

	# output U
	for line in U.data:
		for val in line:
			f1.write(str(val) + ' ')
		f1.write('\n')

	# output V
	for line in V.data:
		for val in line:
			f2.write(str(val) + ' ')
		f2.write('\n')

	# output S
	for val in S:
		f3.write(str(val) + '\n')

	f1.close()
	f2.close()
	f3.close()

	# Code to test Frobenius Norm
	print "Frobenius norm:", frob_norm(A, U, S, V)


if __name__ == '__main__':
	main()


