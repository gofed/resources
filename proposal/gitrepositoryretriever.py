from retriever import Retriever
from git import Repo
import tempfile
import tarfile
import os
import shutil

class GitRepositoryRetriever(Retriever):

	def retrieve(self, repository, protocol = "https"):
		"""Retrieve repository from github.com or bitbucket.org
		The method returns path of retrieved repository.
		Caller is responsible for deleting the path.
		:param username: git username
		:type  username: str
		:param project: git project
		:type  project: str
		:param protocol: protocol based on which a repository get retrieved, e.g. https, git
		:type  protocol: str
		"""
		if protocol == "https":
			provider = repository["provider"]
			if provider == "github":
				clone_url = "https://github.com/%s/%s" % (repository["username"], repository["project"])
			else:
				raise ValueError("Provider '%s' not recognized" % provider)

			clone_dir = tempfile.mkdtemp()

			Repo.clone_from(clone_url, clone_dir)

			# create temp file for tarball 
			with tempfile.NamedTemporaryFile(delete=False) as f:
				# archive the repository
				with tarfile.open(f.name, "w:gz") as tar:
					tar.add(clone_dir, arcname=os.path.basename(clone_dir))
				f.flush()

			# clean the directory
			shutil.rmtree(clone_dir)

			return f.name

		raise ValueError("'%s' protocol unsupported" % protocol)

