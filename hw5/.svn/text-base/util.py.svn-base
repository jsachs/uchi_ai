"""
Utility module for HW5
"""
from __future__ import division
from operator import mul

# Constant enumeration for document classes
Unknown, Hamilton, Madison = range(3)


class Document(object):
	"""Class for a document to be tested or classified"""
	def __init__(self, text, label=0, name = ""):
		self.data = text       # Document converted to a list of its words
		self.label = label     # The class label for a given document
		self.len  = len(text)  # Length of the document, in words
		self.freq = {}         # Dictionary of words and frequencies
		self.name = name

		for word in self.data:
			if self.freq.get(word.lower()):
				self.freq[word.lower()] += 1
			else:
				self.freq[word.lower()] = 1


def load_document(filename):
	ret = []
	lines = open(filename, 'r').readlines()
	for line in lines:
		l = line.split()
		for word in l:
			if '--' in word: # splits words joined by a dash (but not a hyphen)
				word = word.split('--')
				for part in word:
					ret.append(str(part.strip('():.,;"')))
			else:
				ret.append(str(word.strip('():.,;"'))) # strips extra chars
	return ret

def document_class(filename):
	fn = str(filename)
	if 'hamilton' in fn:
		return Hamilton
	elif 'madison' in fn:
		return Madison
	else:
		return Unknown

def prod(factors):
	return reduce(mul, factors, 1)
