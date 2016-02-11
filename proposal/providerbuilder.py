from resources.proposal.storagebuilder import StorageBuilder
from resources.proposal.githubsourcecodeprovider import GithubSourceCodeProvider
from resources.proposal.githubsourcecoderetriever import GithubSourceCodeRetriever

class ProviderBuilder(object):

	def __init__(self):
		pass

	def buildGithubSourceCodeProvider(self):
		# TODO(jchaloup) set storage working directory from configuration
		storage = StorageBuilder().buildGithubSourceCodeStorage("/var/lib/gofed/storage")
		retriever = GithubSourceCodeRetriever()
		provider = GithubSourceCodeProvider(storage, retriever)
		return provider

