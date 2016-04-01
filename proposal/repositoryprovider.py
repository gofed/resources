from provider import Provider
from repositorystorage import RepositoryStorage
from repositoryretriever import RepositoryRetriever
from shutil import move

class RepositoryProvider(Provider):

	def __init__(self, storage, retriever, working_directory):
		"""
		:param storage:	repository storage
		:type  storage: RepositoryStorage
		:param retriever: repository retriever
		:type  retriever: RepositoryRetriever
		"""
		if storage != None and not isinstance(storage, RepositoryStorage):
			raise ResourceInvalidStorageError("RepositoryProvider accepts RepositoryStorage only")

		if not isinstance(retriever, RepositoryRetriever):
			raise ResourceInvalidRetrieverError("RepositoryProvider accepts RepositoryRetriever only")

		Provider.__init__(self, storage, retriever, working_directory)

	def provide(self, repository):
		"""For a given tuple (username, project) provide corresponding resource.
		Source codes can be retrieved from distribution builder
		or from a storage (if available)

		:param repository: repository
		:type  repository: dictionary
		"""

		# check the storage
		if self._storage != None:
			try: 
				return self._storage.retrieve(repository)
			except KeyError:
				pass

		# check distribution builder
		resource_location = self._retriever.retrieve(repository)
		# rename the resource location
		resource_dest = "%s/%s" % (self.working_directory, self.generateUniqueName())
		# TODO(jchaloup): catch exception and throw one with more information?
		move(resource_location, resource_dest)

		if self.storeResource():
			self._storage.store(resource_dest, repository)

		return resource_dest
