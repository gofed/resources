import logging
logger = logging.getLogger("bitbucket_source_code_provider")

from provider import Provider
from .exceptions import ResourceInvalidStorageError, ResourceInvalidRetrieverError, ResourceUnableToRetrieveError
from bitbucketsourcecodestorage import BitbucketSourceCodeStorage
from bitbucketsourcecoderetriever import BitbucketSourceCodeRetriever
from shutil import move

class BitbucketSourceCodeProvider(Provider):
	"""Retrieve source codes from a bitbucket repository (remote or local)
	If a resource is retrieved from a retriever,
	retriever returns location of a temporary file.
	Once the file created, it is a cheap operation to rename the file.
	Provider will then return permanent location under common directory.
	GC can then watch the directory and remove suitable files in it.

	If a resource is retrieved from a storage,
	storage can return location of a temporary file.
	E.g. a resource was from a db in binary and then written into a file.
	If the resource is not temporary file,
	it has permanent location.

	For both cases provider can decide which file needs to be removed.
	Every file contained in the common directory will get removed in
	specified amount of time (1 minute implicitly).

	TODO(jchaloup): implement GC for provider (run as a daemon?)
	"""
	def __init__(self, storage, retriever, working_directory):
		"""
		:param storage:	bitbucket source code storage
		:type  storage: BitbucketSourceCodeStorage
		:param retriever: bitbucket source code retriever
		:type  retriever: BitbucketSourceCodeRetriever
		"""
		if storage != None and not isinstance(storage, BitbucketSourceCodeStorage):
			raise ResourceInvalidStorageError("BitbucketSourceCodeProvider excepts BitbucketSourceCodeStorage only")

		if not isinstance(retriever, BitbucketSourceCodeRetriever):
			raise ResourceInvalidRetrieverError("BitbucketSourceCodeProvider excepts BitbucketSourceCodeRetriever only")

		Provider.__init__(self, storage, retriever, working_directory)

	def provide(self, repository, commit):
		"""For a given pair (repository, commit) provide corresponding resource.
		Source codes can be retrieved from upstream repository, local repository
		or from a storage (if available)

		:param repository:	bitbucket repository signature
		:type  repository:	dict
		:param commit:	commit in the repository
		:type  commit:	str
		"""
		# check the storage
		if self._storage != None:
			logger.info("checking bitbucketsourcecodestorage for %s:%s" % (str(repository), commit))
			try:
				return self._storage.retrieve(repository, commit)
			except KeyError:
				pass

		# TODO(jchaloup) check local repository

		# check upstream repository
		logger.info("retriving resource %s:%s with bitbucketsourcecoderetriever" % (str(repository), commit))
		resource_location = self._retriever.retrieve(repository, commit)
		logger.debug("resource %s:%s retrieved" % (str(repository), commit))

		# rename the resource location
		resource_dest = "%s/%s" % (self.working_directory, self.generateUniqueName())
		# TODO(jchaloup): catch exception and throw one with more information?
		move(resource_location, resource_dest)
		logger.debug("resource %s:%s moved under working directory" % (str(repository), commit))
		return resource_dest

