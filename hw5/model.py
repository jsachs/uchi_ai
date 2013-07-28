"""
Module for Multinomial Models using Naive Bayes
"""
from __future__ import division
from util import Document, prod
from math import log


Unknown, Hamilton, Madison = range(3)


class MultinomialModel(object):
	"""Superclass for Multinomial Models"""
	def __init__(self):
		self.thetas = {}  # Dictionary of P(w|C). w is the key, value is a class dict
		self.pis = {}     # Dictionary of P(C) for a given class C
		self.vocab = {}
		self.num_words = 0
		self.M_tot = {}   # total words in each class

	def classify(self, doc):
		# determine new words for normalization:
		ret = []
		extra = 0
		for w, f in doc.freq.iteritems():
			if not self.thetas.get(w):
				extra += 1

		for key, value in self.pis.iteritems():
			prob = value
			factors = []
			for w, f in doc.freq.iteritems():
				if self.thetas.get(w):  # TODO what if we haven't seen this word before?
					temp = self.thetas.get(w).get(key)/((len(self.vocab) + extra)*self.gamma + self.M_tot[key])
					temp = log(temp)*f
				else:
					temp = self.gamma/((len(self.vocab) + extra)*self.gamma + self.M_tot[key])
					temp = log(temp)*f
				factors.append(temp)
			prob *= sum(factors)
			ret.append((prob, key))
		return ret


class MLE(MultinomialModel):
	"""Frequentist maximum likelihood estimator"""
	def __init__(self, docs, gamma):
		super(MLE, self).__init__()
		self.docs = docs  # a list of Document objects for training
		self.N    = len(docs)
		self.gamma = gamma

	def build_probs(self):
		# Load vocabulary and total words
		for doc in self.docs:
			for key, value in doc.freq.iteritems():
				if self.vocab.get(key):
					self.vocab[key] += value
				else:
					self.vocab[key] = value
				self.num_words += value

		# Determine total words in each class
		for doc in self.docs:
			if self.M_tot.get(doc.label):
				self.M_tot[doc.label] += doc.len
			else:
				self.M_tot[doc.label] = doc.len

		# Determine theta parameters P(w|C)
		for w, value in self.vocab.iteritems():
			vec = {}
			for doc in self.docs:
				if vec.get(doc.label):
					vec[doc.label] += doc.freq.get(w,0)
				else:
					vec[doc.label] = doc.freq.get(w,0)
			for key, value in vec.iteritems():
				vec[key] = (self.gamma + value) # (test comment out) # /(len(self.vocab)*self.gamma + M_tot[key]) # add one smoothing
			self.thetas[w] = vec

		# Set up initial pi parameters P(C)
		hcount = 0
		for doc in self.docs:
			if doc.label == Hamilton:
				hcount += 1
		hprob = hcount/len(self.docs)
		self.pis[Hamilton] = hprob
		self.pis[Madison] = 1-hprob



