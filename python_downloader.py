#
#	I needed a way to download multiple files (images) from nothing more
#	than a text file with links, so I came up with this.
#
#	usage: $ python python_downloader.py listOfUrls.txt
#
import urllib
import sys
from os.path import basename
from urlparse import urlsplit

def url2name(url):
    return basename(urlsplit(url)[2])

def download1(url):
	fileName = url2name(url)
	print "downloading " + localName + " with urllib"
	urllib.urlretrieve(url, localName)

# check to see if an argument (file) has been provided
if (len(sys.argv) > 1):
	with open(sys.argv[1]) as f:
		for line in f:
			line = line.rstrip('\r\n')
			try:
				download1(line)
			except:
				print "error downloading " + line
else:
	print "file argument missing"