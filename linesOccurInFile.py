#!/usr/bin/python

import sys
import os
import random

""" This script will get a listing of all the files in the a directory.
It will create a dictionary of all the file names. It file name will have
a value of next starting number. The second number will be the end number.
The end number will be determined by the number of lines in the file.
A random number will be generated in a range of total line count.
The script will then output the filename where the random number fell
into the list.
"""

fileDict = {}
lineStart = 0

def lineCount(file):
    #print "File: %s" % file
    lines = 0

    for line in open(file):
        lines += 1
    return lines
    #with open(file,"r+") as f:
    #    buffer = mmap.mmap(f.fileno(), 0)
    #    print buffer.readline()
        #readline = buf.readline()
        #while readline():
        #    lines += 1
    #    buffer.close()
    #return lines

def genRandom(total):
    num = int(random.randint(0,total))
    return num

def main():
    totalLines = 0
    lineStart = 0
    path = "/vagrant/testspace/python-learning-2015"
    onlyFiles = [ f for f in os.listdir(path)
    if os.path.isfile(os.path.join(path,f))]
    #print "OnlyFiles: %s" % onlyFiles

    for file in onlyFiles:
        numLines = lineCount(file)
        if numLines == 0:
            continue
        #z  numLines = 5
        print "file: %s Number: %s" % (file,numLines)
        if len(fileDict) != 0:
            #print "line start: %s" % lineStart
            lineStart = totalLines + 1

        totalLines = numLines + totalLines
        print "linestart: %s totalLInes: %s" % (lineStart, totalLines)
        fileDict.setdefault(file,[]).append(lineStart)
        fileDict.setdefault(file,[]).append(totalLines)
        #fileDict[file].append({"Start":lineStart,"End":totalLines})

    randNumber = int(genRandom(totalLines))
    print "Total lines: %s"  % totalLines

    for key in fileDict:
        print key, 'and', fileDict[key][0], 'and', fileDict[key][1]
        if randNumber >= fileDict[key][0] and randNumber <= fileDict[key][1]:
            print "found it in file: %s Random Num: %d " % (key,randNumber)
            break
        else:
            print "Nah: %d" % randNumber




if __name__ == "__main__":
    main()
