#!/bin/python

import sys
from provider import Provider

class SrcRpmProvider(Provider):
	def __init__(self):
		raise NotImplementedError("Cannot instantiate abstract class")

	def provide(self, package, version):
		# let's do it explicitly
		return super(SrcRpmProvider, self).provide(package = package, version = version)

if __name__ == '__main__':
	sys.exit(1)

