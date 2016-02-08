#!/bin/python

import sys

class Receiver(object):
	'''
	Abstract receiver defines what should every implemented *Receiver implement
	'''
	def __init__(self):
		raise NotImplementedError("Cannot instantiate abstract class")

	def receive(self, *args, **kwargs):
		raise NotImplementedError()

if __name__ == '__main__':
	sys.exit(1)

