from storage import Storage

class DirectoryStorage(Storage):

	def __init__(self):
		raise NotImplementedError()

	def store(self, resource_location, resource_id):
		raise NotImplementedError()

	def retrieve(self, resource_id):
		raise NotImplementedError()
