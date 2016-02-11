class Provider(object):

	def __init__(self, storage, retriever):
		self._storage = storage
		self._retriever = retriever

	def provide(self, *args, **kwargs):
		raise NotImplementedError()

