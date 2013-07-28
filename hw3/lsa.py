"""
Module to test latent semantic analysis on the u.data set
"""
from __future__ import division
from sys import argv
from math import sqrt
from random import random, uniform

from matrix import Matrix, load_matrix, dot
from svdP import svd, frob_norm


def get_udata_matrix():
	"""There are 943 users, 1682 movies. This makes the matrix."""
	A = Matrix(943,1682)
	lines = open('ml-100k/u.data','r').readlines()
	for line in lines:
		l = line.split()
		A.data[int(l[0])-1][int(l[1])-1] = int(l[2])
	return A

def main():
	if len(argv) < 2:
		print "Usage: <num eigenvectors>"
		return
	k = int(argv[1])
	A = get_udata_matrix()
	U, S, V = svd(k, 0.01, A)

	print "Frobenius norm:", frob_norm(A, U, S, V)

if __name__ == '__main__':
	main()