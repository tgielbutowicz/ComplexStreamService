import sys
import json
from pprint import pprint

def open_json(data):
    with open(data) as data_file:
        data_json = json.load(data_file)['results']
    return data_json

def search_word(jsonData,dictionary):
    for result in jsonData:
     for data in result['data']:
        for part in data['text'].split():
            if part in dictionary:
                print "JEST : %s" % (part)


if __name__=="__main__":
    oj = open_json('vul_input.json')
    dictionary = ['dupa', 'kurde', 'kurwa']
    pprint(oj)

    print "Znalezione wyrazy"
    sw = search_word(oj,dictionary)





