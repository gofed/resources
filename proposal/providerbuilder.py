from .storagebuilder import StorageBuilder
from .retrieverbuilder import RetrieverBuilder

from .githubsourcecodeprovider import GithubSourceCodeProvider
from .rpmprovider import RpmProvider
from .gitrepositoryprovider import GitRepositoryProvider
from .mercurialrepositoryprovider import MercurialRepositoryProvider

from gofed_resources.proposal.config.config import ResourcesConfig

class ProviderBuilder(object):

	def __init__(self):
		pass

	def buildSourceCodeProvider(self, repository):
		if repository["provider"] == "github":
			return self.buildGithubSourceCodeProvider()

		raise KeyError("Provider '%s' not supported" % repository["provider"])

		if repository["provider"] == "bitbucket":
			return None

	def buildGithubSourceCodeProvider(self):
		storage = StorageBuilder().buildGithubSourceCodeStorage(ResourcesConfig().storageDirectory())
		retriever = RetrieverBuilder().buildGithubSourceCodeRetriever()
		provider = GithubSourceCodeProvider(storage, retriever, ResourcesConfig().providerDirectory())
		return provider

	def buildRpmProvider(self):
		storage = StorageBuilder().buildRpmStorage(ResourcesConfig().storageDirectory())
		retriever = RetrieverBuilder().buildRpmRetriever()
		provider = RpmProvider(storage, retriever, ResourcesConfig().providerDirectory())
		return provider

	def buildGitRepositoryProvider(self):
		storage = StorageBuilder().buildGitRepositoryStorage(ResourcesConfig().storageDirectory())
		retriever = RetrieverBuilder().buildGitRepositoryRetriever()
		provider = GitRepositoryProvider(storage, retriever, ResourcesConfig().providerDirectory())
		return provider

	def buildMercurialRepositoryProvider(self):
		storage = StorageBuilder().buildMercurialRepositoryStorage(ResourcesConfig().storageDirectory())
		retriever = RetrieverBuilder().buildMercurialRepositoryRetriever()
		provider = MercurialRepositoryProvider(storage, retriever, ResourcesConfig().providerDirectory())
		return provider

