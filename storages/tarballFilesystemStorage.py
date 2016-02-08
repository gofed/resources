#!/bin/python

import os
import sys
from filesystemStorage import FilesystemStorage

class TarballFilesystemStorage(FilesystemStorage):
	'''
	TarballFilesystemStorage specifies how are files organized on the filesystem
	and based on it, it implements manipulation with them
	'''
	def _get_filename(self, project, commit):
		return project + '-' + commit[:6] + 'tar.gz'

	def _get_path(self, project, commit):
		filename = self._get_filename(project, commit)
		path = os.path.join(self.get_workdir(), filename)
		return path

	def is_available(self, project, commit):
		path = self._get_path(project, commit)
		return os.path.isfile(path)

	def retrieve(self, project, commit):
		if not self.is_available(project, commit):
			raise KeyError() # TODO: add exception

		path = self._get_path(project, commit)
		with open(path, 'r') as f:
			content = f.read

		return content

	def store(self, content, project, commit):
		path = self._get_path(project, commit)

		with open(path, 'w') as f:
			f.write(content)

if __name__ == '__main__':
	sys.exit(1)

