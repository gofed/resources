from storage import Storage

class RepositoryStorage(Storage):

	def _constructKey(self, *args):
		return Storage._constructKey(self, self.__class__.__name__.lower(), *args)

	def _getKey(self, repository):
		return self._constructKey(repository["provider"], repository["username"], repository["project"])

	def store(self, repository_location, repository):
		"""
		param:	repository_location	file (e.g. tarball) containing the repository
		type:	repository_location	str
		"""
		# possibly construct a key from (username, project) tuple
		key = self._getKey(repository)

		self.storage_obj.store(repository_location, key)

	def retrieve(self, repository):
		# possibly construct a key from (username, project) tuple
		key = self._getKey(repository)

		return self.storage_obj.retrieve(key)

