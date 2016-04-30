import sys 

if __name__ == "gofed_resources":
	sys.modules['resources'] = sys.modules[__name__]
