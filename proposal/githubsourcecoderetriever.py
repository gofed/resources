from retriever import Retriever

class GithubSourceCodeRetriever(Retriever):

	def retrieve(self, repository_url, commit):
		"""Retrieve source codes tarball from github repository.
		The method returns path of retrieved tarball.
		Caller is responsible for deleting the path.
		:param repository_url:	github repository, e.g. github.com/coreos/etcd
		:type  repository_url:	str
		:param commit:	commit in the repository
		:type  commit:	str
		"""
		# TODO(jchaloup): check the repository is valid github repository url

		# construct the download url
		# https://REPOSITORY_URL/archive/COMMIT/name.tar.gz
		tarball_url = "https://%s/archive/%s/name.tar.gz" % (repository_url, commit)

		return self._retrieveResource(tarball_url)

if __name__ == "__main__":
	GithubSourceCodeRetriever().retrieve("github.com/coreos/etcd", "d1b5fdea252dd5e4cafd2e7ccd7c900c2844bbe8")
