from gofed_lib.config.config import Config
from gofed_lib.utils import getScriptDir

class ResourcesConfig(Config):

	def __init__(self):
		Config.__init__(self, "resources.conf")

	def _classDir(self):
		return getScriptDir(__file__)

	def storageDirectory(self):
		return self._config.get("resources", "storage_dir")

	def providerDirectory(self):
		return self._config.get("resources", "provider_dir")

