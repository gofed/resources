from retriever import Retriever
import urllib2
import tempfile
from ..exceptions import ResourceInvalidResourceError

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

		# TODO(jchaloup): catch exceptions: urllib2.URLError, urllib2.HTTPError
		#	raise ResourceNotRetrieved instead?
		try:
			response = urllib2.urlopen(tarball_url)
		except urllib2.URLError as err:
			# can a user do something about it?
			msg = "Unable to retrieve resource, url = %s, err = " % (tarball_url, err)
			raise urllib2.URLError(msg)
		except urllib2.HTTPError as err:
			# can a user do something about it?
			msg = "Unable to retrieve resource, url = %s, err = " % (tarball_url, err)
			raise urllib2.HTTPError(msg)

		try:
			with tempfile.NamedTemporaryFile(delete=False) as f:
				f.write(response.read())
				f.flush()
		except IOError as e:
			# can a user do something about it?
			msg = "Unable to store retrieved resource, err = " % (err)
			raise ResourceUnableToRetrieveError(msg)

		return f.name

if __name__ == "__main__":
	GithubSourceCodeRetriever().retrieve("github.com/coreos/etcd", "d1b5fdea252dd5e4cafd2e7ccd7c900c2844bbe8")
