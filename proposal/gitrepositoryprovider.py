from .repositoryprovider import RepositoryProvider
from .gitrepositorystorage import GitRepositoryStorage
from .gitrepositoryretriever import GitRepositoryRetriever
from shutil import move
from ..exceptions import ResourceInvalidStorageError, ResourceInvalidRetrieverError

class GitRepositoryProvider(RepositoryProvider):

	def __init__(self, storage, retriever, working_directory):
		"""
		:param storage:	github repository storage
		:type  storage: GithubRepositoryStorage
		:param retriever: github repository retriever
		:type  retriever: GithubRepositoryRetriever
		:param working_directory: working directory for provider
		:type  working_directory: string
		"""
		if storage != None and not isinstance(storage, GitRepositoryStorage):
			raise ResourceInvalidStorageError("GitRepositoryProvider accepts GitRepositoryStorage only")

		if not isinstance(retriever, GitRepositoryRetriever):
			raise ResourceInvalidRetrieverError("GitRepositoryProvider accepts GitRepositoryRetriever only")

		RepositoryProvider.__init__(self, storage, retriever, working_directory)

