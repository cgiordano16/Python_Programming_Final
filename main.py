#!/user/bin/python

import sys
import os
import os.path
import json
import readJSComments
import requests
import configparser

def main():
    # TODO Testing for python files

    relativePath = str(sys.argv[1])
    fileType = str(sys.argv[2])

    if (fileType.lower() == 'js' or fileType.lower() == 'py'):
        readJSComments.recursiveDir(relativePath, fileType)

if __name__ == "__main__":
    main()
