from storage import Storage

class RpmStorage(Storage):

	def store(self, rpm_location, product, distribution, build, nvr):
		# construct key from (product, distribution, build, nvr) tuple
		key = self._constructKey(product, distribution, build, nvr)

		self.storage_obj.store(rpm_location, key)

	def retrieve(self, product, distribution, build, nvr):
		# construct key from (product, distribution, build, nvr) tuple
		key = self._constructKey(product, distribution, build, nvr)

		return self.storage_obj.retrieve(key)
