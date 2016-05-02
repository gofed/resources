from retriever import Retriever
import tempfile
import tarfile
import os
import shutil

class RepositoryRetriever(Retriever):

	def _cloneRepository(self, clone_url, clone_dir):
		"""Clone repository

		:param clone_url: repository clone url
		:type  clone_url: string
		:param clone_dir: directory to clone repository to
		:type  clone_dir: string
		"""
		raise NotImplementedError()

	def _constructCloneURL(self, repository, protocol):
		"""Construct clone url for given repository

		:param repository: repository
		:type  repository: dictionary
		:param protocol: protocol
		:type  protocol: string
		"""
		raise NotImplementedError()

	def retrieve(self, repository, protocol = "https"):
		"""Retrieve repository from github.com or bitbucket.org
		The method returns path of retrieved repository.
		Caller is responsible for deleting the path.
		:param repository: repository
		:type  repository: dictionary
		:param protocol: protocol based on which a repository get retrieved, e.g. https, git
		:type  protocol: str
		"""
		clone_url = self._constructCloneURL(repository, protocol)
		clone_dir = tempfile.mkdtemp()
		self._cloneRepository(clone_url, clone_dir)

		# create temp file for tarball 
		with tempfile.NamedTemporaryFile(delete=False) as f:
			# archive the repository
			with tarfile.open(f.name, "w:gz") as tar:
				tar.add(clone_dir, arcname=os.path.basename(clone_dir))
			f.flush()

		# clean the directory
		shutil.rmtree(clone_dir)

		return f.name


