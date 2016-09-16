import logging
logger = logging.getLogger("github_source_code_provider")

from .sourcecodeprovider import SourceCodeProvider
from .exceptions import ResourceInvalidStorageError, ResourceInvalidRetrieverError, ResourceUnableToRetrieveError
from .githubsourcecodestorage import GithubSourceCodeStorage
from .githubsourcecoderetriever import GithubSourceCodeRetriever
from shutil import move

class GithubSourceCodeProvider(SourceCodeProvider):

	def __init__(self, storage, retriever, working_directory):
		"""
		:param storage:	github source code storage
		:type  storage: GithubSourceCodeStorage
		:param retriever: github source code retriever
		:type  retriever: GithubSourceCodeRetriever
		"""
		if storage != None and not isinstance(storage, GithubSourceCodeStorage):
			raise ResourceInvalidStorageError("GithubSourceCodeProvider excepts GithubSourceCodeStorage only")

		if not isinstance(retriever, GithubSourceCodeRetriever):
			raise ResourceInvalidRetrieverError("GithubSourceCodeProvider excepts GithubSourceCodeRetriever only")

		SourceCodeProvider.__init__(self, storage, retriever, working_directory)

