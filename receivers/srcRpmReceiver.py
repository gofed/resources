#!/bin/python

import sys
from receiver import Receiver

class SrcRpmReceiver(Receiver):
	def __init__(self):
		pass

	def receive(self, package, arch):
		# TODO: implement
		return str(package + arch)

if __name__ == '__main__':
	sys.exit(1)

