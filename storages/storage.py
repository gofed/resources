#!/bin/python

import sys

class Storage(object):
	'''
	Abstract storage defines what should every storage implement
	'''
	def __init__(self):
		raise NotImplementedError("Cannot instantiate abstract class")

	def is_available(self, *args, **kwargs):
		raise NotImplementedError()

	def retrieve(self, *args, **kwargs):
		raise NotImplementedError()

	def store(self, *args, **kwargs):
		raise NotImplementedError()

	def set_space_limit(self, limit):
		raise NotImplementedError()

	def get_total_space(self):
		raise NotImplementedError()

	def get_free_space(self):
		raise NotImplementedError()

	def get_used_space(self):
		raise NotImplementedError()

if __name__ == '__main__':
	sys.exit(1)

