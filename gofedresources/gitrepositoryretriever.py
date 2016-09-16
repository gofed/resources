from .repositoryretriever import RepositoryRetriever
from git import Repo

class GitRepositoryRetriever(RepositoryRetriever):

	def _cloneRepository(self, clone_url, clone_dir):
		"""Clone repository

		:param clone_url: repository clone url
		:type  clone_url: string
		:param clone_dir: directory to clone repository to
		:type  clone_dir: string
		"""
		Repo.clone_from(clone_url, clone_dir)

	def _constructCloneURL(self, repository, protocol):
		"""Construct clone url for given repository

		:param repository: repository
		:type  repository: dictionary
		:param protocol: protocol
		:type  protocol: string
		"""
		provider = repository["provider"]
		if provider not in ["github"]:
			raise ValueError("Provider '%s' not supported" % provider)

		if protocol == "https":
			return "https://github.com/%s/%s" % (repository["username"], repository["project"])
		else:
			raise ValueError("Protocol '%s' not supported" % provider)

