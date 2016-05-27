import logging
logger = logging.getLogger("bitbucket_source_code_provider")

from sourcecodeprovider import SourceCodeProvider
from .exceptions import ResourceInvalidStorageError, ResourceInvalidRetrieverError, ResourceUnableToRetrieveError
from bitbucketsourcecodestorage import BitbucketSourceCodeStorage
from bitbucketsourcecoderetriever import BitbucketSourceCodeRetriever

class BitbucketSourceCodeProvider(SourceCodeProvider):

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

		SourceCodeProvider.__init__(self, storage, retriever, working_directory)

