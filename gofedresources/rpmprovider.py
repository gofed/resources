from .provider import Provider
from .rpmstorage import RpmStorage
from .rpmretriever import RpmRetriever
from shutil import move

class RpmProvider(Provider):

	def __init__(self, storage, retriever, working_directory):
		"""
		:param storage:	github source code storage
		:type  storage: GithubSourceCodeStorage
		:param retriever: github source code retriever
		:type  retriever: GithubSourceCodeRetriever
		"""
		if storage != None and not isinstance(storage, RpmStorage):
			raise ResourceInvalidStorageError("RpmProvider excepts RpmStorage only")

		if not isinstance(retriever, RpmRetriever):
			raise ResourceInvalidRetrieverError("RpmProvider excepts RpmRetriever only")

		Provider.__init__(self, storage, retriever, working_directory)

	def provide(self, product, distribution, build, rpm):
		"""For a given tuple (product, distribution, build, rpm) provide corresponding resource.
		Source codes can be retrieved from distribution builder
		or from a storage (if available)

		:param product:	os product, e.g. Fedora, CentOS
		:type  product:	str
		:param distribution:	os version, e.g. f23, centos7
		:type  distribution:	str
		:param build:	build nvr, e.g. etcd-2.2.2-1
		:type  build:	str
		:param rpm:	rpm, e.g. etcd-devel-2.2.2-4.fc24.noarch.rpm
		:type  rpm:	str
		"""

		# check the storage
		if self._storage != None:
			try: 
				return self._storage.retrieve(product, distribution, build, rpm)
			except KeyError:
				pass

		# check distribution builder
		resource_location = self._retriever.retrieve(product, distribution, build, rpm)
		# rename the resource location
		resource_dest = "%s/%s" % (self.working_directory, self.generateUniqueName())
		# TODO(jchaloup): catch exception and throw one with more information?
		move(resource_location, resource_dest)
		return resource_dest
