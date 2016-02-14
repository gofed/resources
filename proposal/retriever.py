import urllib2
import tempfile
from ..exceptions import ResourceUnableToRetrieveError

class Retriever(object):

	def retrieve(self, *args):
		raise NotImplementedError()

	def _retrieveResource(self, resource_url):
		# TODO(jchaloup): catch exceptions: urllib2.URLError, urllib2.HTTPError
		#	raise ResourceNotRetrieved instead?
		try:
			response = urllib2.urlopen(resource_url)
		except urllib2.URLError as err:
			# can a user do something about it?
			msg = "Unable to retrieve resource, url = %s, err = " % (resource_url, err)
			raise urllib2.URLError(msg)
		except urllib2.HTTPError as err:
			# can a user do something about it?
			msg = "Unable to retrieve resource, url = %s, err = " % (resource_url, err)
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

