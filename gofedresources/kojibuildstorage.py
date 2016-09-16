from .storage import Storage

class KojiBuildStorage(Storage):

	def _constructKey(self, *args):
		return Storage._constructKey(self, self.__class__.__name__.lower(), *args)

	def store(self, build_location, product, distribution, build):
		"""
		param:	build_location	tarball containing build's (s)rpms
		type:	build_location	str
		"""
		# construct a key from (product, distribution, build) tuple
		key = self._constructKey(product, distribution, build)

		self.storage_obj.store(build_location, key)

	def retrieve(self, product, distribution, build):
		# construct a key from (product, distribution, build) tuple
		key = self._constructKey(product, distribution, build)

		return self.storage_obj.retrieve(key)
