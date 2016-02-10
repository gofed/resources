from storage import Storage

class SpecfileStorage(Storage):

	def store(self, specfile_location, product, distribution, nvr):
		# construct a key from (product, distribution, nvr) tuple
		key = self._constructKey(product, distribution, nvr)

		self.storage_obj.store(specfile_location, key)

	def retrieve(self, product, distribution, nvr):
		# construct a key from (product, distribution, nvr) tuple
		key = self._constructKey(product, distribution, nvr)

		return self.storage_obj.retrieve(key)

