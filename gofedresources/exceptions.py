import sys

class ResourcesGenericException(Exception):
	pass

class ResourcesBadProject(ResourcesGenericException):
	pass

class ResourcesBadCommit(ResourcesGenericException):
	pass

class ResourcesNoSpace(ResourcesGenericException):
	pass

class ResourceNotFoundError(ResourcesGenericException):
	pass

class ResourceInvalidStorageError(ResourcesGenericException):
	pass

class ResourceInvalidRetrieverError(ResourcesGenericException):
	pass

class ResourceUnableToRetrieveError(ResourcesGenericException):
	pass

class ResourceUnableToStoreError(ResourcesGenericException):
	pass

class ResourceInvalidResourceError(ResourcesGenericException):
	pass


if __name__ == '__main__':
	sys.exit(1)

