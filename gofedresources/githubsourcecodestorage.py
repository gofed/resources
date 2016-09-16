from .storage import Storage
from gofed_lib.urlbuilder.builder import UrlBuilder

class GithubSourceCodeStorage(Storage):

	def _constructKey(self, *args):
		return Storage._constructKey(self, self.__class__.__name__.lower(), *args)

	def store(self, source_code_location, repository, commit):
		# construct a key from (project, repository_url, commit) tuple
		repository_url = UrlBuilder().buildGithubProvider(repository)
		key = self._constructKey(repository_url, commit)

		self.storage_obj.store(source_code_location, key)

	def retrieve(self, repository, commit):
		# construct a key from (project, repository_url, commit) tuple
		repository_url = UrlBuilder().buildGithubProvider(repository)
		key = self._constructKey(repository_url, commit)

		return self.storage_obj.retrieve(key)

