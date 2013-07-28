"""
Module to implement utility functions for hw6
"""
from __future__ import division
from math import sqrt
from random import random
import operator


def load_graph(filename):
	"""Loads a graph from an ASCII file to a Graph class"""
	image = []
	lines = open(filename, 'r').readlines()
	for line in lines:
		line = line.split()
		temp = []
		for num in line:
			temp.append(int(num))
		image.append(temp)
	return image

def corrupt_image(graph, mu):
	"""Introduces random noise to a Graph image"""
	def flip():
		return True if random() < mu else False
	N = graph.N
	for i in range(N):
		for j in range(N):
			if flip():
				val = graph.nodes[i*N + j].val
				if val == 1:
					graph.nodes[i*N + j].val = 0
				else:
					graph.nodes[i*N + j].val = 1

def output_graph(graph):
	"""Prints the current Graph to the standard out"""
	N = graph.N
	for i in range(N):
		row = ''
		for j in range(N):
			val = graph.nodes[i*N + j].val
			if val == 1:
				row += '*'
			else:
				row += ' '
		print row
	return

def build_disc(filename):
	"""Constructs a disc image file to be loaded"""
	with open(filename, 'w') as f:
		for i in range(100):
			for j in range(100):
				dist = sqrt( (i-50)**2 + (j-50)**2 )
				if dist <= 40:
					f.write(str(1))
				else:
					f.write(str(0))
				f.write(' ')
			f.write('\n')
		f.close()
	return

def build_disc_small(filename):
	"""Constructs a disc image file to be loaded"""
	with open(filename, 'w') as f:
		for i in range(50):
			for j in range(50):
				dist = sqrt( (i-25)**2 + (j-25)**2 )
				if dist <= 20:
					f.write(str(1))
				else:
					f.write(str(0))
				f.write(' ')
			f.write('\n')
		f.close()
	return

def compare_graphs(g1, g2):
	"""Function to calculate similarity (accuracy) from reconstruction"""
	same = 0
	diff = 0
	N = g1.N
	for i in range(N):
		for j in range(N):
			v1 = g1.nodes[i*N + j].val
			v2 = g2.nodes[i*N + j].val
			if v1==v2:
				same += 1
			else:
				diff += 1
	return same/(same+diff)

def prod(items):
    return reduce(operator.mul, items, 1)

