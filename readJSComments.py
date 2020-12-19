#!/user/bin/python

import sys
import os
import os.path
import requests
import configparser
import requests
import json

def recursiveDir(startingDir, fileType):
    for rootDir, dirs, files in os.walk(startingDir, topdown=False):
        for thisFile in files:
            fullName = os.path.join(rootDir, thisFile)
            if ('node_modules' in fullName) != True:
                if os.path.splitext(thisFile)[1] == '.js' and fileType == 'js':
                    processJSFile(os.path.join(rootDir, thisFile), '//')
                elif os.path.splitext(thisFile)[1] == '.py' and fileType == 'py':
                    processJSFile(os.path.join(rootDir, thisFile), '#')

def processJSFile(jsFile, commentType):
    commentString = commentType
    toDoString = 'TODO'
    openJS = open(jsFile, 'r')
    readJS = openJS.readlines()
    for line in readJS:
        if toDoString in line.upper() and commentString in line:
            trelloRequest(line, jsFile)

def trelloRequest(line, lineFile):
    config = configparser.ConfigParser()
    config.read('env.ini')

    allBoardsUrl = 'https://api.trello.com/1/members/me/boards'
    thisBoardUrl = 'https://api.trello.com/1/boards/{}/lists'
    createCardUrl = 'https://api.trello.com/1/cards'
    
    headers = {
        'Accept': 'application/json'
    }
    print(config['default']['key'])
    allBoardsParams = {
        'fields': 'name',
        'key': config['default']['key'],
        'token': config['default']['token'],
    }
    thisBoardParams = {
        'key': config['default']['key'],
        'token': config['default']['token'],
    }

    allBoards = requests.request('GET', allBoardsUrl, headers=headers, params=allBoardsParams)

    for board in json.loads(allBoards.text):
        if board['name'] == config['default']['board_name']:
            allLists = requests.request('GET', thisBoardUrl.format(board['id']), headers=headers, params=thisBoardParams)
            postCardParams = {
                'key': config['default']['key'], 
                'token': config['default']['token'], 
                'idList': json.loads(allLists.text)[0]['id'],
                'name': lineFile,
                'desc': line
            }
            postCard = requests.request('POST', createCardUrl, params=postCardParams)