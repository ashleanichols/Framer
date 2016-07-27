#!/usr/bin/env python
import os
import sys

"""

brew install imagemagick --with-jp2
brew install webp

"""

path = os.path.join("extras", "DeviceResources")
jp2_quality = 16
webp_quality = 90

os.chdir(path)
os.system("rm *.jp2")
os.system("rm *.webp")

for fileName in os.listdir("."):
	if fileName.endswith(".png"):
		print fileName
		os.system("sips -s format jp2 %s -s formatOptions %s --out %s" % (fileName, jp2_quality, fileName.replace(".png", ".jp2")))
		os.system("cwebp -q %s '%s' -o '%s'" % (webp_quality, fileName, fileName.replace(".png", ".webp")))
