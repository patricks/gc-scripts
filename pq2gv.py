#!/usr/bin/env python
#
# Copyright 2011 Patrick Steiner <patrick@helmsdeep.at>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


__author__ =  "Patrick Steiner"
__version__ = "1.0.0"

# file handling
import os
import codecs

# command line args
import sys

# xml
from xml.dom.minidom import parse

################################################################################

class GpxReader(object):
	def getText(self, nodelist):
		rc = ""
		for node in nodelist:
			if node.nodeType == node.TEXT_NODE:
				rc = rc + node.data
		return rc

	def handleWaypointName(self, wpt):
		return "%s" % self.getText(wpt.childNodes)

	def convert(self, filename):
		pqfile = filename
		
		if os.path.exists(pqfile):
			print "Reading file one moment..."

			dom = parse(pqfile)
			count = 0
			f = codecs.open("gc_visits.txt", "w", "utf-8")

			for node in dom.getElementsByTagName("wpt"):
				count += 1
				name = self.handleWaypointName(node.getElementsByTagName("name")[0])
				date = self.handleWaypointName(node.getElementsByTagName("groundspeak:date")[0])

				print "Processing: " + str(count) + ": " + name
				#print "DBG:" + name + "," + date +",Found it,\"\""
				f.write( name + "," + date +",Found it,\"\"\n")

			print str(count) + " caches processed."

			f.close()
		else:
			print "ERROR: " + pqfile + " doesn't exist"

################################################################################

def main():
	if len(sys.argv) == 2:
		pqfile = sys.argv[1]

		gpx = GpxReader()
		gpx.convert(pqfile)
	else:
		print "Usage: pg2gv pocketquery.gpx"

if __name__ == "__main__":
    main()

# vim:ts=4:sw=4:
