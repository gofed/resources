from directorystorage import DirectoryStorage
from filestorage import FileStorage
from specfilestorage import SpecfileStorage
from tarballstorage import TarballStorage
from githubsourcecodestorage import GithubSourceCodeStorage

class StorageBuilder(object):

	def __init__(self):
		pass

	def buildSpecfileStorage(self, work_dir):
		obj = DirectoryStorage(work_dir)
		obj = FileStorage(obj)
		obj = SpecfileStorage(obj)
		return obj

	def buildGithubSourceCodeStorage(self, work_dir):
		obj = DirectoryStorage(work_dir)
		obj = TarballStorage(obj)
		obj = GithubSourceCodeStorage(obj)
		return obj
	
