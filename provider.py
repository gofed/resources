#!/bin/python

import sys

class Provider(object):
	def __init__(self):
		self._storage = None
		self._receiver = None
		raise NotImplementedError("Cannot instantiate abstract class")

	def is_cached(self, *args, **kwargs):
		return self._storage.is_available(*args, **kwargs)

	def set_storage_space_limit(self, limit):
		self._storage.set_space_limit(limit)

	def get_storage_total_space(self):
		return self._storage.get_total_space()

	def get_storage_used_space(self):
		return self._storage.get_used_space()

	def get_storage_free_space(self):
		return self._storage.get_free_space()

	def provide(self, *args, **kwargs):
		if not self._storage.is_available(*args, **kwargs):
			content = self._receiver.receive(*args, **kwargs)
			self._storage.store(content, *args, **kwargs)

		return self._storage.retrieve(*args, **kwargs)

if __name__ == '__main__':
	sys.exit(1)

