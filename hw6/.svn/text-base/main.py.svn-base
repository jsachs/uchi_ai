"""
Main module for message passing hw6
"""
from test import *


def main():

	"""
	Proof-of-concept test

	Shows a pure disc, the corrupted disc,
	then performs reconstruction and prints
	the cleaned-up disc.
	Meant to show visually that this works
	"""
	visual_test()

	"""
	Testing for mu and theta

	Tests different values of theta on different values of mu
	"""
	for mu in [0.1, 0.2, 0.3, 0.4, 0.5]:
		for theta in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
			parameter_test(mu, theta)

	return

if __name__ == '__main__':
	main()