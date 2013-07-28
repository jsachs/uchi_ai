"""
Module implementing test functions
"""
from __future__ import division
from model import MLE

# Constant enumeration for document classes
Unknown, Hamilton, Madison = range(3)

stopwords = ['the', 'of', 'and', 'to', 'in', 'i', 'that', 'was', 'his', 'he']


""" ================
Main Project
====================
"""

"""
Cross-validation for gamma
"""
def pick_gamma(training_list):
	for gamma in range(1,30):
		right = 0
		wrong = 0
		for l in range(len(training_list)):
			copy = list(training_list)
			test = copy.pop(l)
			mle = MLE(copy, gamma)
			mle.build_probs()
			labels = mle.classify(test)
			c = max(labels)[1]
			# print labels, c, test.label
			if c == test.label:
				right += 1
			else:
				wrong += 1
		print "Gamma:", gamma
		print "Accuracy:", right/(right+wrong)

"""
Cross-validation with chosen parameters
"""
def test_params(training_list):
	gamma = 5
	right = 0
	wrong = 0
	for l in range(len(training_list)):
		copy = list(training_list)
		test = copy.pop(l)
		mle = MLE(copy, gamma)
		mle.build_probs()
		labels = mle.classify(test)
		c = max(labels)[1]
		print "Document:", test.name
		print "Hamilton:", labels[0][0], "| Madison:", labels[1][0]
		if c == 1:
			print "Classified: Hamilton"
		else:
			print "Classified: Madison"
		if test.label == 1:
			print "Actual: Hamilton"
		else:
			print "Actual: Madison"
		if c == test.label:
			right += 1
		else:
			wrong += 1
	print "Gamma:", gamma
	print "Accuracy:", right/(right+wrong)

"""
Unknown document testing
"""
def test_classify(training_list, test_list):
	gamma = 5
	mle = MLE(training_list, gamma)
	mle.build_probs()
	for l in range(len(test_list)):
		labels = mle.classify(test_list[l])
		c = max(labels)[1]
		print "Document:", test_list[l].name
		print "Hamilton:", labels[0][0], "| Madison:", labels[1][0]
		if c == 1:
			print "Classified: Hamilton"
		else:
			print "Classified: Madison"


"""
Cross-validation for omitted words
"""
def pick_gamma_ec(training_list):
	for gamma in range(1,10):
		right = 0
		wrong = 0
		for l in range(len(training_list)):
			copy = list(training_list)
			test = copy.pop(l)
			mle = MLE(copy, gamma)

			for word in stopwords:
				if word in mle.vocab:
					mle.num_words -= mle.vocab[word]
					del mle.vocab[word]
				if word in test.freq:
					test.len -= test.freq[word]
					del test.freq[word]
				for doc in mle.docs:
					if word in doc.freq:
						doc.len -= doc.freq[word]
						del doc.freq[word]

			mle.build_probs()
			labels = mle.classify(test)
			c = max(labels)[1]
			# print labels, c, test.label
			if c == test.label:
				right += 1
			else:
				wrong += 1
		print "Gamma:", gamma
		print "Accuracy:", right/(right+wrong)

"""
Cross-validation with chosen parameters
"""
def test_params_ec(training_list):
	gamma = 5
	right = 0
	wrong = 0
	for l in range(len(training_list)):
		copy = list(training_list)
		test = copy.pop(l)
		mle = MLE(copy, gamma)

		for word in stopwords:
			if word in mle.vocab:
				mle.num_words -= mle.vocab[word]
				del mle.vocab[word]
			if word in test.freq:
				test.len -= test.freq[word]
				del test.freq[word]
			for doc in mle.docs:
				if word in doc.freq:
					doc.len -= doc.freq[word]
					del doc.freq[word]

		mle.build_probs()
		labels = mle.classify(test)
		c = max(labels)[1]
		print "Document:", test.name
		print "Hamilton:", labels[0][0], "| Madison:", labels[1][0]
		if c == 1:
			print "Classified: Hamilton"
		else:
			print "Classified: Madison"
		if test.label == 1:
			print "Actual: Hamilton"
		else:
			print "Actual: Madison"
		if c == test.label:
			right += 1
		else:
			wrong += 1
	print "Gamma:", gamma
	print "Accuracy:", right/(right+wrong)

"""
Unknown document testing
"""
def test_classify_ec(training_list, test_list):
	gamma = 5
	mle = MLE(training_list, gamma)

	for word in stopwords:
		if word in mle.vocab:
			mle.num_words -= mle.vocab[word]
			del mle.vocab[word]
		for doc in mle.docs:
			if word in doc.freq:
				doc.len -= doc.freq[word]
				del doc.freq[word]

	mle.build_probs()
	for l in range(len(test_list)):
		test = test_list[l]

		if word in test.freq:
			test.len -= test.freq[word]
			del test.freq[word]

		labels = mle.classify(test)
		c = max(labels)[1]
		print "Document:", test.name
		print "Hamilton:", labels[0][0], "| Madison:", labels[1][0]
		if c == 1:
			print "Classified: Hamilton"
		else:
			print "Classified: Madison"



