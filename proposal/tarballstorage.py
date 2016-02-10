from storage import Storage

class TarballStorage(Storage):

	def store(self, tarball_location, tarball_id):
		# possibly construct a key from tarball_id
		key = constructKey(tarball_id)

		self.storage_obj.store(tarball_location, key)

	def retrieve(self, tarball_id):
		# possibly construct a key from tarball_id
		key = constructKey(tarball_id)

		return self.storage_obj.retrieve(key)
