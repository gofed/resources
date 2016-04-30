import uuid
from resources.proposal.config.config import ResourcesConfig

class Provider(object):

	def __init__(self, storage, retriever, working_directory):
		self._storage = storage
		self._retriever = retriever
		self.working_directory = working_directory

		# store retrieved resources
		self.store = ResourcesConfig().cacheResources()

	def storeResource(self):
		return self.store

	def provide(self, *args, **kwargs):
		raise NotImplementedError()

	def generateUniqueName(self):
		return "%s-%s%s" % (
			self.__class__.__name__.lower(),
			uuid.uuid4().hex,
			uuid.uuid4().hex
		)
