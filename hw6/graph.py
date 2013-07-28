"""
Module to implement a graph structure for hw6
"""
from __future__ import division
from util import *


class Graph(object):
	"""Implementation of an MRF Graph"""
	def __init__(self, image):
		self.N = len(image)  # dimension of graph
		self.nodes = []      # simple list of nodes
		for i in range(self.N):
			for j in range(self.N):
				self.nodes.append(Node(image[i][j], i, j, self.N, self))

	def get_node(self, i, j):
		"""Method to return a specific MRF node"""
		node = self.nodes[i*self.N + j]
		return node

	def loopy_bp(self, theta):
		"""Method to execute the loopy belief propagation algorithm"""
		t = 0
		while 1:
			# Collect
			for node in self.nodes:
				node.collect(t, theta)
			# Get marginals, check for convergence
			converge = True
			for node in self.nodes:
				m0, m1 = node.marginals()
				if abs(m0-node.marg_0) > 0.01 or abs(m1-node.marg_1) > 0.01:
					converge = False
				node.marg_0 = m0
				node.marg_1 = m1
			if converge or t > 30:  # Convergence reached
				for node in self.nodes:
					# Change pixels for marginals
					if node.marg_1 > node.marg_0:
						node.val = 1
					else:
						node.val = 0
				break
			t += 1
		return t


class Node(object):
	"""Implementation of an MRF Node"""
	def __init__(self, val, i, j, N, G):
		self.val = val  # 0 or 1 (value of corresponding observed variable)
		self.i   = i    # x coordinate
		self.j   = j    # y coordinate
		self.N   = N    # image (graph) dimension
		self.G   = G    # parent graph

		# message history
		self.msg_0 = {}
		self.msg_1 = {}

		# marginal history
		self.marg_0 = 0
		self.marg_1 = 0

		# Sets up the neigbors for the unobserved node
		if i==0 and j==0:
			self.neighbors = [(0,1), (1,0)]
		elif i==0 and j==N-1:
			self.neighbors = [(0,N-2), (1,N-1)]
		elif i==N-1 and j==0:
			self.neighbors = [(N-1,1), (N-2,0)]
		elif i==N-1 and j==N-1:
			self.neighbors = [(N-1,N-2), (N-2,N-1)]
		elif i==0:
			self.neighbors = [(0,j-1), (0,j+1), (1,j)]
		elif i==N-1:
			self.neighbors = [(N-1,j-1), (N-1,j+1), (N-2,j)]
		elif j==0:
			self.neighbors = [(i-1,0), (i+1,0), (i,1)]
		elif j==N-1:
			self.neighbors = [(i-1,N-1), (i+1,N-1), (i,N-2)]
		else:
			self.neighbors = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]

	def collect(self, t, theta):
		"""Method to collect messages from neighbors"""
		# 0-valued messages
		if t==0:
			for n in self.neighbors:
				self.msg_0[n] = 1
			self.msg_0['y'] = phi(self.val, 0, theta)
		else:
			for n in self.neighbors:
				denom = self.get_unnorm_msg(n, 0, theta) + self.get_unnorm_msg(n, 1, theta)
				num   = self.get_unnorm_msg(n, 0, theta)
				self.msg_0[n] = num/denom

		# 1-valued messages
		if t==0:
			for n in self.neighbors:
				self.msg_1[n] = 1
			self.msg_1['y'] = phi(self.val, 1, theta)
		else:
			for n in self.neighbors:
				denom = self.get_unnorm_msg(n, 0, theta) + self.get_unnorm_msg(n, 1, theta)
				num   = self.get_unnorm_msg(n, 1, theta)
				self.msg_1[n] = num/denom

	def marginals(self):
		"""Return the marginals for this node"""
		# 0-valued marginal
		temp = []
		for key, value in self.msg_0.iteritems():
			temp.append(value)
		m0 = prod(temp)

		# 1-valued marginal
		temp = []
		for key, value in self.msg_1.iteritems():
			temp.append(value)
		m1 = prod(temp)

		return m0, m1

	def get_unnorm_msg(self, neighbor, val, theta):
		"""Returns the normalized message from neighbor"""
		n = self.G.get_node(neighbor[0], neighbor[1])
		# 0-message
		temp = []
		for w in n.neighbors:
			if self.i!=w[0] and self.j!=w[1]:
				temp.append(n.msg_0[w])
		temp.append(n.msg_0['y'])
		r0 = phi(0, val, theta) * prod(temp)

		# 1-message
		temp = []
		for w in n.neighbors:
			if self.i!=w[0] and self.j!=w[1]:
				temp.append(n.msg_1[w])
		temp.append(n.msg_1['y'])
		r1 = phi(1, val, theta) * prod(temp)

		return r0+r1


def phi(i, j, theta):
	"""Potential function"""
	if i==j:
		return 1 + theta
	else:
		return 1 - theta

