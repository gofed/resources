from provider import Provider
from githubrepositorystorage import GithubRepositoryStorage
from githubrepositoryretriever import GithubRepositoryRetriever
from shutil import move

class GithubRepositoryProvider(Provider):

	def __init__(self, storage, retriever, working_directory):
		"""
		:param storage:	github repository storage
		:type  storage: GithubRepositoryStorage
		:param retriever: github repository retriever
		:type  retriever: GithubRepositoryRetriever
		"""
		if storage != None and not isinstance(storage, GithubRepositoryStorage):
			raise ResourceInvalidStorageError("GithubRepositoryProvider excepts GithubRepositoryStorage only")

		if not isinstance(retriever, GithubRepositoryRetriever):
			raise ResourceInvalidRetrieverError("GithubRepositoryProvider excepts GithubRepositoryRetriever only")

		Provider.__init__(self, storage, retriever, working_directory)

	def provide(self, username, project):
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
				return self._storage.retrieve(username, project)
			except KeyError:
				pass

		# check distribution builder
		resource_location = self._retriever.retrieve(username, project)
		# rename the resource location
		resource_dest = "%s/%s" % (self.working_directory, self.generateUniqueName())
		# TODO(jchaloup): catch exception and throw one with more information?
		move(resource_location, resource_dest)
		return resource_dest
