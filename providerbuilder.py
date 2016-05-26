from .storagebuilder import StorageBuilder
from .retrieverbuilder import RetrieverBuilder

from .githubsourcecodeprovider import GithubSourceCodeProvider
from .bitbucketsourcecodeprovider import BitbucketSourceCodeProvider

from .rpmprovider import RpmProvider
from .gitrepositoryprovider import GitRepositoryProvider
from .mercurialrepositoryprovider import MercurialRepositoryProvider

from .config.config import ResourcesConfig

class ProviderBuilder(object):

	def __init__(self):
		pass

	def buildSourceCodeProvider(self, repository):
		if repository["provider"] == "github":
			return self.buildGithubSourceCodeProvider()
		if repository["provider"] == "bitbucket":
			return self.buildBitbucketSourceCodeProvider()

		raise KeyError("Provider '%s' not supported" % repository["provider"])

	def buildGithubSourceCodeProvider(self):
		storage = StorageBuilder().buildGithubSourceCodeStorage(ResourcesConfig().storageDirectory())
		retriever = RetrieverBuilder().buildGithubSourceCodeRetriever()
		provider = GithubSourceCodeProvider(storage, retriever, ResourcesConfig().providerDirectory())
		return provider

	def buildBitbucketSourceCodeProvider(self):
		storage = StorageBuilder().buildBitbucketSourceCodeStorage(ResourcesConfig().storageDirectory())
		retriever = RetrieverBuilder().buildBitbucketSourceCodeRetriever()
		provider = BitbucketSourceCodeProvider(storage, retriever, ResourcesConfig().providerDirectory())
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

