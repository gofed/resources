from storage import Storage

class GithubSourceCodeStorage(Storage):

	def store(self, source_code_location, project, repository, commit):
		# construct a key from (project, repository, commit) tuple
		key = self._constructKey(project, repository, commit)

		self.storage_obj.store(source_code_location, key)

	def retrieve(self, project, repository, commit):
		# construct a key from (project, repository, commit) tuple
		key = self._constructKey(project, repository, commit)

		return self.storage_obj.retrieve(key)

