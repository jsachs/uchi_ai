"""
Main module for HW5
"""
from util import Document, load_document, document_class
from model import MLE
from test import *
import os

# Constant enumeration for document classes
Unknown, Hamilton, Madison = range(3)


def main():
	# Build a Document list
	training = []
	for filename in os.listdir('federalist/'):
		dc = document_class(filename)
		if dc in (Hamilton, Madison):
			d = Document(load_document('federalist/' + filename), dc, filename)
			training.append(d)

	# Build the testing list
	test = []
	for filename in os.listdir('federalist/'):
		dc = document_class(filename)
		if dc == Unknown and 'txt' in filename:
			d = Document(load_document('federalist/' + filename), dc, filename)
			test.append(d)

	"""
	Determination of appropriate gamma
	"""
	print "Gamma selection"
	pick_gamma(training)

	"""
	Checking cross-validatino with chosen params
	"""
	print "Parameter testing"
	test_params(training)

	"""
	Classifying documents
	"""
	print "Classification"
	test_classify(training, test)

	""" ================
	Extra Credit
	====================
	"""
	print ""
	print "================"
	print "EXTRA CREDIT VALIDATION"
	print "================"

	print "Gamma selection"
	pick_gamma_ec(training)

	print "Parameter testing"
	test_params_ec(training)

	print "Classification"
	test_classify_ec(training, test)


	return

if __name__ == '__main__':
	main()