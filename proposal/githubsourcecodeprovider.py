from provider import Provider
from ..exceptions import ResourceInvalidStorageError, ResourceInvalidRetrieverError, ResourceUnableToRetrieveError
from githubsourcecodestorage import GithubSourceCodeStorage
from githubsourcecoderetriever import GithubSourceCodeRetriever
from shutil import move

class GithubSourceCodeProvider(Provider):
	"""Retrieve source codes from a github repository (remote or local)
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
		:param storage:	github source code storage
		:type  storage: GithubSourceCodeStorage
		:param retriever: github source code retriever
		:type  retriever: GithubSourceCodeRetriever
		"""
		if storage != None and not isinstance(storage, GithubSourceCodeStorage):
			raise ResourceInvalidStorageError("GithubSourceCodeProvider excepts GithubSourceCodeStorage only")

		if not isinstance(retriever, GithubSourceCodeRetriever):
			raise ResourceInvalidRetrieverError("GithubSourceCodeProvider excepts GithubSourceCodeRetriever only")

		Provider.__init__(self, storage, retriever, working_directory)

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
		resource_location = self._retriever.retrieve(repository_url, commit)
		# rename the resource location
		resource_dest = "%s/%s" % (self.working_directory, self.generateUniqueName())
		# TODO(jchaloup): catch exception and throw one with more information?i
		move(resource_location, resource_dest)
		return resource_dest
