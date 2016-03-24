from storage import Storage

class GithubRepositoryStorage(Storage):

	def _constructKey(self, username, project):
		return Storage._constructKey(self, "github-repository", username, project)

	def store(self, repository_location, username, project):
		"""
		param:	repository_location	file (e.g. tarball) containing the repository
		type:	repository_location	str
		"""
		# possibly construct a key from (username, project) tuple
		key = self._constructKey(username, project)

		self.storage_obj.store(repository_location, key)

	def retrieve(self, username, project):
		# possibly construct a key from (username, project) tuple
		key = self._constructKey(username, project)

		return self.storage_obj.retrieve(key)

