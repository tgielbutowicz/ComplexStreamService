import sys
import json
import re
from pprint import pprint
from collections import Counter


def open_json(data):
    with open(data) as data_file:
        data_json = json.load(data_file)['results']
    return data_json


def search_word(jsonData, dictionary):
    cnt = Counter()
    temp = []
    for result in jsonData:
        for data in result['data']:
            for part in data['text'].split():
                if part in dictionary:
                    temp.insert(0,data['ip'])
                    temp.insert(1,data['port'])
                    cnt[part] += 1
            return cnt, temp


def put(ip, port,site, data, filename):
    try:
        jsondata = json.dumps({'ip': ip, 'port': port, 'word': data})
        fd = open(filename, 'w')
        fd.write(jsondata)
        fd.close()
    except:
        print 'ERROR writing', filename
        pass


if __name__ == "__main__":
    oj = open_json('vul_input.json')
    dictionary = ['dupa', 'kurde', 'kurwa']
    pprint(oj)

    print "Znalezione wyrazy:"
    sw,tt = search_word(oj, dictionary)
    for key, value in sw.items():
       print "%s | count: %s" % (key, value)


    put(tt.__getitem__(0), tt.__getitem__(1), sw.items(), 'vul_output.json')











