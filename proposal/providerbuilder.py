from .storagebuilder import StorageBuilder
from .retrieverbuilder import RetrieverBuilder

from .githubsourcecodeprovider import GithubSourceCodeProvider
from .rpmprovider import RpmProvider
from .gitrepositoryprovider import GitRepositoryProvider
from .mercurialrepositoryprovider import MercurialRepositoryProvider

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
		# TODO(jchaloup) set storage working directory from configuration
		storage = StorageBuilder().buildGithubSourceCodeStorage("/var/lib/gofed/storage")
		retriever = RetrieverBuilder().buildGithubSourceCodeRetriever()
		# TODO(jchaloup) set storage working directory from configuration
		provider = GithubSourceCodeProvider(storage, retriever, "/var/lib/gofed/resource_provider")
		return provider

	def buildRpmProvider(self):
		# TODO(jchaloup) set storage working directory from configuration
		storage = StorageBuilder().buildRpmStorage("/var/lib/gofed/storage")
		retriever = RetrieverBuilder().buildRpmRetriever()
		# TODO(jchaloup) set storage working directory from configuration
		provider = RpmProvider(storage, retriever, "/var/lib/gofed/resource_provider")
		return provider

	def buildGitRepositoryProvider(self):
		# TODO(jchaloup) set storage working directory from configuration
		storage = StorageBuilder().buildGitRepositoryStorage("/var/lib/gofed/storage")
		retriever = RetrieverBuilder().buildGitRepositoryRetriever()
		# TODO(jchaloup) set storage working directory from configuration
		provider = GitRepositoryProvider(storage, retriever, "/var/lib/gofed/resource_provider")
		return provider

	def buildMercurialRepositoryProvider(self):
		# TODO(jchaloup) set storage working directory from configuration
		storage = StorageBuilder().buildMercurialRepositoryStorage("/var/lib/gofed/storage")
		retriever = RetrieverBuilder().buildMercurialRepositoryRetriever()
		# TODO(jchaloup) set storage working directory from configuration
		provider = MercurialRepositoryProvider(storage, retriever, "/var/lib/gofed/resource_provider")
		return provider

