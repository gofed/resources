#!/bin/python

import sys
from provider import Provider
from receivers.tarballReceiver import TarballReceiver
from storages.tarballFilesystemStorage import TarballFilesystemStorage

class TarballProvider(Provider):
	def __init__(self, work_dir):
		self._receiver = TarballReceiver()
		self._storage = TarballFilesystemStorage(work_dir)

	def provide(self, project, commit):
		# let's do it explicitly
		return super(TarballProvider, self).provide(project = project, commit = commit)

if __name__ == '__main__':
	# just for testing purposes, will be deleted
	print 'this is ilustrating how a user will use resources package'
	project = 'golang-github-armon-gomdb'
	commit = '151f2e08ef45cb0e57d694b2562f351955dff572'
	work_dir = 'tmp'

	print 'provide(%s, %s) use working dir %s' % (project, commit, work_dir)
	foo = TarballProvider(work_dir)

	print "is tarball in the storage (is cached?)"
	print foo.is_cached(project, commit)

	foo.provide(project, commit)

	print "is tarball in the storage (is cached?)"
	print foo.is_cached(project, commit)

	print "And there will be an exception - a user wants to get project, which does not exist"
	print "There will be 'Resources' defined exception, since we don't want to be dependend on external dependencies (they can change)"
	foo.provide('golang-github-foo-gomdb', commit)

	sys.exit(1)

