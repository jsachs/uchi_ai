"""
Module to test perceptron performance
"""
from lin_per import LinearPerceptron as LP
from ker_per import KernelPerceptron as KP


def load_file(filename):
	"""Loads number/label data into perceptron readable format"""
	lines = open(filename,'r').readlines()
	ret = []
	for line in lines:
		new = []
		line = line.strip()
		line = line.split(' ')
		for num in line:
			new.append(int(num))
		ret.append(new)
	return ret

def test1(data, labels):
	"""Online test of linear perceptron"""
	p1 = LP()
	right, wrong, error = p1.train_online(data, labels)
	print "Right:", right
	print "Wrong:", wrong
	print "Error:", error
	return

def test2(data, labels, test_data):
	"""Batch test of linear perceptron"""
	p2 = LP()
	it, err = p2.train_batch(data, labels)
	print "Iterations:", it
	print "Error:", err
	p2.label_test(test_data)
	return

def test3(data, labels, sigma):
	"""Online test of kernel perceptron"""
	p3 = KP(data, labels)
	right, wrong, error = p3.train_online(sigma)
	print "Right:", right
	print "Wrong:", wrong
	print "Error:", error
	return

def test4(data, labels, test_data, sigma):
	"""Batch test of kernel perceptron"""
	p4 = KP(data, labels)
	it, err = p4.train_batch(sigma)
	print "Iterations:", it
	print "Error:", err
	p4.label_test(test_data, sigma)
	return


def main():
	data = load_file('train2k.databw.35')
	labels = load_file('train2k.label.35')
	test_data = load_file('test200.databw.35')

	"""
	test1

	Perceptron: Linear
	Mode: Online

	Runs the linear perceptron on the 2k set,
	printing the right and wrong predictions
	to the standard out after a single pass.

	The test also produces the 'linear_online.txt'
	file with the number of mistakes made as a function
	of the examples seen.
	"""
	print "=============================="
	print "Linear Perceptron"
	print "Online Mode"
	test1(data, labels)
	print "=============================="
	print '\n'

	"""
	test2

	Perceptron: Linear
	Mode: Batch

	Runs the linear perceptron on the 2k set,
	printing the right and wrong predictions
	to the standard out after many Iterations
	over the data.

	After finishing running on the training
	set, this test produces the 'test200.label.35'
	file with the predicted labels for the test data.
	"""
	print "=============================="
	print "Linear Perceptron"
	print "Batch Mode"
	test2(data, labels, test_data)
	print "=============================="
	print '\n'

	"""
	test3

	Perceptron: Kernel
	Mode: Online

	Runs the kernel perceptron on the 2k set,
	printing the right and wrong predictions
	to the standard out after a single pass.

	The test also produces the 'kernel_online.txt'
	file with the number of mistakes made as a function
	of the examples seen.

	For reference, I have left commented the code
	used to determine the best sigma.
	"""
	sigma = 4.4

	print "=============================="
	print "Kernel Perceptron"
	print "Online Mode"
	test3(data, labels, sigma)
	print "=============================="
	print '\n'

	# while sigma < 5:
	# 	print "=============================="
	# 	print "Kernel Perceptron"
	# 	print "Online Mode"
	# 	print "Sigma:", sigma
	# 	test3(data, labels, sigma)
	# 	print "=============================="
	# 	print '\n'
	# 	sigma += 1

	"""
	test4

	Perceptron: Kernel
	Mode: Batch

	Runs the kernel perceptron on the 2k set,
	printing the right and wrong predictions
	to the standard out after many Iterations
	over the data.

	After finishing running on the training
	set, this test produces the 'test200.label.35'
	file with the predicted labels for the test data.
	"""
	print "=============================="
	print "Kernel Perceptron"
	print "Batch Mode"
	test4(data, labels, test_data, sigma)
	print "=============================="
	print '\n'

if __name__ == '__main__':
	main()




