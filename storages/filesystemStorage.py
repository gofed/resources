#!/bin/python

import sys, os
from storage import Storage

class FilesystemStorage(Storage):
	'''
	FilesystemStorage only knows a location of a working directory ("a
	contact point" like DatabaseStorage)
	'''
	def __init__(self, work_dir):
		self._work_dir = work_dir

		if not os.path.isdir(work_dir):
			os.mkdir(work_dir)

	def get_workdir(self):
		return self._work_dir

if __name__ == '__main__':
	sys.exit(1)

