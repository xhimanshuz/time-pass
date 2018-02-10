#!/usr/bin/python2.7
#Copy file1 to file2
from sys import argv
from os.path import exists
source, filenamein, filenameout = argv
print("Copy %r text to %r" %(filenamein, filenameout))
print("Opening File...")
ofilein = open(filenamein, "r")
print("Check %r Exists? %r" %   (filenameout, exists(filenameout)));
ofileout = open(filenameout, "w")
print("%r is %r Bytes" %(filenamein, len(filenamein)))
#readfile = ofilein.read()
ofileout.write(ofilein.read())
print("Copying is completed!")
ofilein.close()
ofileout.close()
