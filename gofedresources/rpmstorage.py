from .storage import Storage

class RpmStorage(Storage):

	def store(self, rpm_location, product, distribution, build, rpm):
		# construct key from (product, distribution, build, nvr) tuple
		key = self._constructKey(product, distribution, build, rpm)

		self.storage_obj.store(rpm_location, key)

	def retrieve(self, product, distribution, build, rpm):
		# construct key from (product, distribution, build, nvr) tuple
		key = self._constructKey(product, distribution, build, rpm)

		return self.storage_obj.retrieve(key)
