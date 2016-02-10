class Storage(Object):

	def __init__(self, storage_obj = None):
		self.storage_obj = storage_obj

	def store(self, resource_location, *args):
		"""
		args must contain resource_id or must be a touple of values
		from which the method can construct resource ID
		"""
		raise NotImplementedError()

	def retrieve(self, resource_id):
		"""
		returns:	resource_location (str)
		"""
		raise NotImplementedError()
