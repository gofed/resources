from retriever import Retriever
from gofed_lib.urlbuilder.builder import UrlBuilder

class GithubSourceCodeRetriever(Retriever):

	def retrieve(self, repository, commit):
		"""Retrieve source codes tarball from github repository.
		The method returns path of retrieved tarball.
		Caller is responsible for deleting the path.
		:param repository:	github repository signature
		:type  repository:	dict
		:param commit:	commit in the repository
		:type  commit:	str
		"""

		# construct the download url
		tarball_url = UrlBuilder().buildGithubSourceCodeTarball(
			repository["username"],
			repository["project"],
			commit
		)

		return self._retrieveResource(tarball_url)

