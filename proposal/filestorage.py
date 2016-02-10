from storage import Storage

class FileStorage(Storage):

	def store(self, file_location, file_id):
		# possibly construct a key from file_id
		key = constructKey(file_id)

		self.storage_obj.store(file_location, key)

	def retrieve(self, file_id):
		# possibly construct a key from file_id
		key = constructKey(file_id)

		return self.storage_obj.retrieve(key)



