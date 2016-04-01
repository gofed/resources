from provider import Provider
from gitrepositorystorage import GitRepositoryStorage
from gitrepositoryretriever import GitRepositoryRetriever
from shutil import move

class GitRepositoryProvider(Provider):

	def __init__(self, storage, retriever, working_directory):
		"""
		:param storage:	github repository storage
		:type  storage: GithubRepositoryStorage
		:param retriever: github repository retriever
		:type  retriever: GithubRepositoryRetriever
		"""
		if storage != None and not isinstance(storage, GitRepositoryStorage):
			raise ResourceInvalidStorageError("GitRepositoryProvider accepts GitRepositoryStorage only")

		if not isinstance(retriever, GitRepositoryRetriever):
			raise ResourceInvalidRetrieverError("GitRepositoryProvider accepts GitRepositoryRetriever only")

		Provider.__init__(self, storage, retriever, working_directory)

	def provide(self, repository):
		"""For a given tuple (username, project) provide corresponding resource.
		Source codes can be retrieved from distribution builder
		or from a storage (if available)

		:param username: github username
		:type  username: str
		:param project: github project
		:type  project: str
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
