from storage import Storage

class GithubRepositoryStorage(Storage):

	def store(self, repository_location, project, repository):
		"""
		param:	repository_location	file (e.g. tarball) containing the repository
		type:	repository_location	str
		"""
		# possibly construct a key from (project, repository) tuple
		key = constructKey(project, repository)

		self.storage_obj.store(repository_location, key)

	def retrieve(self, project, repository):
		"""
		param:	repository_location	file (e.g. tarball) containing the repository
		type:	repository_location	str
		"""
		# possibly construct a key from (project, repository) tuple
		key = constructKey(project, repository)

		return self.storage_obj.retrieve(key)

