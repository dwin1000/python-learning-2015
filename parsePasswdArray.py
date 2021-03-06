#!/usr/bin/env python
import os.path
import sys

"""
This script attempts to open up the passwd file and look
for any uid that appears multiple times. if true then it
echo out the associated usernames
"""
file = "passwd"
#def splitLines():
dictUser = {}

def main():
    retFlag = os.path.exists(file)
    print "retFlag = ", retFlag
    if not retFlag:
        print "Couldn't find the file: (%s) anywhere" % file
        sys.exit(0)
    else:
        print "Found file...continuing"

    try:
        fileHandle = open(file,"r+")
        print "Name of the file: ", fileHandle.name
        print "mode of the file: ", fileHandle.mode

        for line in fileHandle:
            #strip new lines
            newLine = line.rstrip('\n')
            print "Line: %s" % newLine
            listLine = newLine.split(":")
            user = listLine[0];
            uid = listLine[2];
            gid = listLine[3];
            print "User: ", user, " | Uid: ", uid, " | Gid: ", gid
            dictUser.setdefault(uid,[]).append(user)

    finally:
        fileHandle.close()

    for key in dictUser:
        if len(dictUser[key]) > 1 :
            print 'UID: ', key, ' and ', dictUser[key], ' and length ', len(dictUser[key])

if __name__ == "__main__":
    main()
