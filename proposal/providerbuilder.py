from storagebuilder import StorageBuilder
from githubsourcecodeprovider import GithubSourceCodeProvider
from githubsourcecoderetriever import GithubSourceCodeRetriever
from rpmretriever import RpmRetriever
from rpmprovider import RpmProvider
from gitrepositoryprovider import GitRepositoryProvider
from gitrepositoryretriever import GitRepositoryRetriever

class ProviderBuilder(object):

	def __init__(self):
		pass

	def buildGithubSourceCodeProvider(self):
		# TODO(jchaloup) set storage working directory from configuration
		storage = StorageBuilder().buildGithubSourceCodeStorage("/var/lib/gofed/storage")
		retriever = GithubSourceCodeRetriever()
		# TODO(jchaloup) set storage working directory from configuration
		provider = GithubSourceCodeProvider(storage, retriever, "/var/lib/gofed/resource_provider")
		return provider

	def buildRpmProvider(self):
		# TODO(jchaloup) set storage working directory from configuration
		storage = StorageBuilder().buildRpmStorage("/var/lib/gofed/storage")
		retriever = RpmRetriever()
		# TODO(jchaloup) set storage working directory from configuration
		provider = RpmProvider(storage, retriever, "/var/lib/gofed/resource_provider")
		return provider

	def buildGitRepositoryProvider(self):
		# TODO(jchaloup) set storage working directory from configuration
		storage = StorageBuilder().buildGitRepositoryStorage("/var/lib/gofed/storage")
		retriever = GitRepositoryRetriever()
		# TODO(jchaloup) set storage working directory from configuration
		provider = GitRepositoryProvider(storage, retriever, "/var/lib/gofed/resource_provider")
		return provider

