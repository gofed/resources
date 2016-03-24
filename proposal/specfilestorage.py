from storage import Storage

class SpecfileStorage(Storage):

	def _constructKey(self, *args):
		return Storage._constructKey(self, self.__class__.__name__.lower(), *args)

	def store(self, specfile_location, product, distribution, nvr):
		# construct a key from (product, distribution, nvr) tuple
		key = self._constructKey(product, distribution, nvr)

		self.storage_obj.store(specfile_location, key)

	def retrieve(self, product, distribution, nvr):
		# construct a key from (product, distribution, nvr) tuple
		key = self._constructKey(product, distribution, nvr)

		return self.storage_obj.retrieve(key)

