from provider import Provider
from ..exceptions import ResourceInvalidStorageError, ResourceInvalidRetrieverError, ResourceUnableToRetrieveError
from githubsourcecodestorage import GithubSourceCodeStorage
from githubsourcecoderetriever import GithubSourceCodeRetriever

class GithubSourceCodeProvider(Provider):
	"""Retrieve source codes from a github repository (remote or local)
	
	"""
	def __init__(self, storage, retriever):
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

		self._storage = storage
		self._retriever = retriever


	def provide(self, repository_url, commit):
		"""For a given pair (repository_url, commit) provide corresponding resource.
		Source codes can be retrieved from upstram repository, local repository
		or from a storage (if available)

		:param repository_url:	github repository, e.g. github.com/coreos/etcd
		:type  repository_url:	str
		:param commit:	commit in the repository
		:type  commit:	str
		"""
		# check the storage
		if self._storage != None:
			try: 
				return self._storage.retrieve(repository_url, commit)
			except KeyError:
				pass

		# TODO(jchaloup) check local repository
		
		# check upstream repository
		return self._retriever.retrieve(repository_url, commit)

