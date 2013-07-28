"""
Module to implement test code for hw6
"""
from graph import Graph, Node
from util import *


def visual_test():
	print "===================="
	print "Visual Test: Small Disc"
	print "===================="
	sdisc = 'sdisc.txt'
	build_disc_small(sdisc)

	print "Original disc:"
	g1 = Graph(load_graph(sdisc))
	graph = Graph(load_graph(sdisc))
	output_graph(graph)

	print "Corrupted disc:"
	corrupt_image(graph, 0.1)
	output_graph(graph)

	print "Reconstructed disc:"
	theta = 0.5
	t = graph.loopy_bp(theta)
	output_graph(graph)
	print "Accuracy:", compare_graphs(g1, graph)
	print "Total iterations:", t
	print "===================="

	print "===================="
	print "Visual Test: Disc"
	print "===================="
	disc = 'disc.txt'
	build_disc(disc)

	print "Original disc:"
	g1 = Graph(load_graph(disc))
	graph = Graph(load_graph(disc))
	output_graph(graph)

	print "Corrupted disc:"
	corrupt_image(graph, 0.1)
	output_graph(graph)

	print "Reconstructed disc:"
	theta = 0.5
	t = graph.loopy_bp(theta)
	output_graph(graph)
	print "Accuracy:", compare_graphs(g1, graph)
	print "Total iterations:", t
	print "===================="

def parameter_test(mu, theta):
	disc = 'disc.txt'
	build_disc(disc)
	print "===================="
	print "Mu:", mu
	print "Theta:", theta
	g1 = Graph(load_graph(disc))
	graph = Graph(load_graph(disc))
	corrupt_image(graph, mu)
	t = graph.loopy_bp(theta)
	print "Accuracy:", compare_graphs(g1, graph)
	print "Total iterations:", t
