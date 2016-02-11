from storage import Storage

class GithubSourceCodeStorage(Storage):

	def store(self, source_code_location, repository_url, commit):
		# construct a key from (project, repository_url, commit) tuple
		key = self._constructKey(repository_url, commit)

		self.storage_obj.store(source_code_location, key)

	def retrieve(self, repository_url, commit):
		# construct a key from (project, repository_url, commit) tuple
		key = self._constructKey(repository_url, commit)

		return self.storage_obj.retrieve(key)

