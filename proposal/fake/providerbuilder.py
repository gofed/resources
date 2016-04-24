from ..providerbuilder import ProviderBuilder
import os

class FakeProviderBuilder(object):

	def __init__(self):
		pass

	def buildSourceCodeProvider(self, provider):
		return self

	def buildGithubSourceCodeProvider(self):
		return self

	def buildRpmProvider(self):
		return self

	def buildGitRepositoryProvider(self):
		return self

	def buildMercurialRepositoryProvider(self):
		return self

	def __getattr__(self, name):
		if name == "provide":
			return self.provide

		raise AttributeError("Method '%s' not found" % name)

	def provide(self, *args):
		return "resource/location"

