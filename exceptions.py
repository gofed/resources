#!/bin/python

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

if __name__ == '__main__':
	sys.exit(1)

