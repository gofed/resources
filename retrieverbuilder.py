from gitrepositoryretriever import GitRepositoryRetriever
from mercurialrepositoryretriever import MercurialRepositoryRetriever
from githubsourcecoderetriever import GithubSourceCodeRetriever
from bitbucketsourcecoderetriever import BitbucketSourceCodeRetriever
from rpmretriever import RpmRetriever

class RetrieverBuilder(object):

	def __init__(self):
		pass

	def buildGitRepositoryRetriever(self):
		return GitRepositoryRetriever()

	def buildMercurialRepositoryRetriever(self):
		return MercurialRepositoryRetriever()

	def buildGithubSourceCodeRetriever(self):
		return GithubSourceCodeRetriever()

	def buildBitbucketSourceCodeRetriever(self):
		return BitbucketSourceCodeRetriever()

	def buildRpmRetriever(self):
		return RpmRetriever()
