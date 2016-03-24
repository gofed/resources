from retriever import Retriever
from git import Repo
import tempfile
import tarfile
import os
import shutil

class GithubRepositoryRetriever(Retriever):

	def retrieve(self, username, project, protocol = "https"):
		"""Retrieve repository from github.com
		The method returns path of retrieved repository.
		Caller is responsible for deleting the path.
		:param username: github username
		:type  username: str
		:param project: github project
		:type  project: str
		:param protocol: protocol based on which a repository get retrieved, e.g. https, git
		:type  protocol: str
		"""
		if protocol == "https":
			clone_url = "https://github.com/%s/%s" % (username, project)
			clone_dir = tempfile.mkdtemp()

			Repo.clone_from(clone_url, clone_dir)
			print clone_dir

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

