from storage import Storage
from binarystorage import BinaryStorage

# create GHSourceCode storage with source codes in tarball storing resource as binary data into e.g. database
def getBinaryGHSourceCodeStorage():
	# as binary data
	storage = BinaryStorage()
	# in tarballs
	storage = TarballStorage(storage)
	# for source code
	storage = GithubSourceCodeStorage(storage)
	return storage

# create GHSourceCode storage with source codes in tarball storing resource as tarball in a file system directory
def getDirectoryGHSourceCodeStorage():
	# as tarball in a directory
	storage = DirectoryStorage()
	# in tarballs
	storage = TarballStorage(storage)
	# for source code
	storage = GithubSourceCodeStorage(storage)
	return storage

# create Specfile storage storing resource as file
def getDirectoryGHSourceCodeStorage():
	# as file in a directory
	storage = DirectoryStorage()
	# in a file
	storage = FileStorage(storage)
	# for a spec file
	storage = SpecfileStorage(storage)
	return storage

