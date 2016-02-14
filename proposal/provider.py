import uuid

class Provider(object):

	def __init__(self, storage, retriever, working_directory):
		self._storage = storage
		self._retriever = retriever
		self.working_directory = working_directory

	def provide(self, *args, **kwargs):
		raise NotImplementedError()

	def generateUniqueName(self):
		return "%s-%s%s" % (
			self.__class__.__name__.lower(),
			uuid.uuid4().hex,
			uuid.uuid4().hex
		)
