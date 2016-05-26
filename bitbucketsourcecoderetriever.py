from retriever import Retriever
from gofed_lib.urlbuilder.builder import UrlBuilder

class BitbucketSourceCodeRetriever(Retriever):

	def retrieve(self, repository, commit):
		"""Retrieve source codes tarball from bitbucket repository.
		The method returns path of retrieved tarball.
		Caller is responsible for deleting the path.
		:param repository:	bitbucket repository signature
		:type  repository:	dict
		:param commit:	commit in the repository
		:type  commit:	str
		"""

		# construct the download url
		tarball_url = UrlBuilder().buildBitbucketSourceCodeTarball(
			repository["username"],
			repository["project"],
			commit
		)

		return self._retrieveResource(tarball_url)

