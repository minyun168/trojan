#

import os

def run(**args):
	print "[*] In invironment module."
	return str(os.environ)
