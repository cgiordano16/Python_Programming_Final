#!/user/bin/python

import sys
import os
import os.path
import json
import readJSComments
import requests
import configparser

def main():
    # TODO Get rid of commented crap
    # config = configparser.ConfigParser()
    # config.read('env.ini')
    # allBoardsUrl = 'https://api.trello.com/1/members/me/boards'
    # thisBoardUrl = 'https://api.trello.com/1/boards/{}/lists'
    # createCardUrl = 'https://api.trello.com/1/cards'
    
    # headers = {
    #     'Accept': 'application/json'
    # }
    # print(config['default']['key'])
    # allBoardsParams = {
    #     'fields': 'name',
    #     'key': config['default']['key'],
    #     'token': config['default']['token'],
    # }
    # thisBoardParams = {
    #     'key': config['default']['key'],
    #     'token': config['default']['token'],
    # }

    # allBoards = requests.request('GET', allBoardsUrl, headers=headers, params=allBoardsParams)

    # for board in json.loads(allBoards.text):
    #     if board['name'] == config['default']['board_name']:
    #         allLists = requests.request('GET', thisBoardUrl.format(board['id']), headers=headers, params=thisBoardParams)
    #         postCardParams = {
    #             'key': config['default']['key'], 
    #             'token': config['default']['token'], 
    #             'idList': json.loads(allLists.text)[0]['id'],
    #             'name': 'Testing Card',
    #             'desc': 'Please work, Please work, PLEASE WORK!!'
    #         }
    #         postCard = requests.request('POST', createCardUrl, params=postCardParams)
    # print(json.loads(allBoards.text))

    relativePath = str(sys.argv[1])
    fileType = str(sys.argv[2])

    if (fileType.lower() == 'js' or fileType.lower() == 'py'):
        readJSComments.recursiveDir(relativePath, fileType)

if __name__ == "__main__":
    main()