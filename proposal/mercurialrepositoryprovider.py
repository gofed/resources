from .repositoryprovider import RepositoryProvider
from .mercurialrepositorystorage import MercurialRepositoryStorage
from .mercurialrepositoryretriever import MercurialRepositoryRetriever
from shutil import move
from ..exceptions import ResourceInvalidStorageError, ResourceInvalidRetrieverError

class MercurialRepositoryProvider(RepositoryProvider):

	def __init__(self, storage, retriever, working_directory):
		"""
		:param storage:	mercurial repository storage
		:type  storage: MercurialRepositoryStorage
		:param retriever: mercurial repository retriever
		:type  retriever: MercurialRepositoryRetriever
		:param working_directory: working directory for provider
		:type  working_directory: string
		"""
		if storage != None and not isinstance(storage, MercurialRepositoryStorage):
			raise ResourceInvalidStorageError("MercurialRepositoryProvider accepts MercurialRepositoryStorage only")

		if not isinstance(retriever, MercurialRepositoryRetriever):
			raise ResourceInvalidRetrieverError("MercurialRepositoryProvider accepts MercurialRepositoryRetriever only")

		RepositoryProvider.__init__(self, storage, retriever, working_directory)

