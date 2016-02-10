from storage import Storage
from shutil import copyfile
from os.path import exists
from ..exceptions import ResourceNotFoundError

class DirectoryStorage(Storage):

	def __init__(self, work_dir):
		"""
		:param	work_dir:	working directory, must exists
		:type	str
		"""
		self.work_dir = work_dir

	def store(self, resource_location, resource_id):
		"""Store resource under working directory
		:param	resource_location:	local path to a resource (to file)
		:type	str
		:param	resource_id:	resource identifier unique to working directory
		:type	str
		"""
		resource_dest = "%s/%s" % (self.work_dir, resource_id)
		# if file exists, rewrite the file
		copyfile(resource_location, resource_dest)
		# TODO(jchaloup): set the file read only
		# TODO(jchaloup): rather throw ResourceStoreError than IOError

	def retrieve(self, resource_id):
		"""Retrieve resource from working directory
		:param	resource_id:	resource identifier
		:type	str
		:returns:	resource location
		:rtype:	str
		"""
		resource_dest = "%s/%s" % (self.work_dir, resource_id)
		# does the resource exists?
		if not exists(resource_dest):
			raise ResourceNotFoundError("Resource %s does not exist, work_dir: %s" % (resource_id, self.work_dir))
		# returns location of a file in a storage (read only)
		return resource_dest

