#!/bin/python

import sys, os
from storage import Storage

class DatabaseStorage(Storage):
	'''
	DatabaseStorage only knows where is a database located (e.g. connection to
	a database, username, password, etc. and how to connect to a database so this
	can be reused in every *DatabaseStorage (which will handle how are data
	stored and received)

	This will give you a power to create SshStorage, FtpStorage,... which will be
	classes describing how to connect to a storage.
	'''
	def __init__(self, database, collection, username = None, password = None):
		raise NotImplementedError()

	def get_connection(self):
		raise NotImplementedError()

if __name__ == '__main__':
	sys.exit(1)

