from storage import Storage

class UserDirectoryStorage(Storage):

	def store(self, directory_location, directory_id):
		# possibly construct a key from directory_id
		key = self._constructKey(directory_id)

		self.storage_obj.store(directory_location, key)

	def retrieve(self, directory_id):
		# possibly construct a key from directory_id
		key = self._constructKey(directory_id)

		return self.storage_obj.retrieve(key)

