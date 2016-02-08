#!/bin/python

import sys, urllib2
from receiver import Receiver

class TarballReceiver(Receiver):
	def __init__(self):
		pass

	def _project2repo(self, package_name):
		ret = None
		parts = package_name.split('-')

		if parts[0] != 'golang':
			raise NotImplementedError() # TODO: this should be a bad package name exception

		# TODO: implemente bitbucket/googlecode/... and mapping handling...
		if parts[1] == 'github':
			if len(parts) < 4:
				raise NotImplementedError()
			# TODO: handle - in project name, e.g.: 'golang', 'github', 'armon', 'go-radix'
			ret = 'https://github.com/%s/%s/' % (parts[2], parts[3])
		else:
			raise NotImplementedError()

		return ret

	def receive(self, project, commit):
		upstream_url = self._project2repo(project)
		upstream_url += "/archive/%s.tar.gz" % commit[:8]

		# TODO: remove
		print upstream_url

		response = urllib2.urlopen(upstream_url)
		return response.read()

if __name__ == '__main__':
	sys.exit(1)

