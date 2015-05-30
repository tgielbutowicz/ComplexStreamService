__author__ = 'Sandra'

import sys
import json
import re
from pprint import pprint
from collections import Counter


def open_json(data):
    with open(data) as data_file:
        data_json = json.load(data_file)['results']
    return data_json


def search_word(jsonData, dictionary, ):
    cnt = Counter()
    temp = []
    for result in jsonData:
        for data in result['data']:
            for part in data['text'].split():
                if part in dictionary:
                    temp.insert(0,data['ip'])
                    temp.insert(1,data['port'])
                    temp.insert(2,data['site'])
                    cnt[part] += 1
            return cnt, temp

def get_net_target(page):
    start_link=page.find("a href")
    start_quote=page.find('q',start_link)
    end_quote=page.find('q',start_quote+1)
    url=page[start_quote+1:end_quote]

    return url



def put(ip, port,site, data, filename):
    try:
        jsondata = json.dumps({'ip': ip, 'port': port,'site':site, 'word': data})
        fd = open(filename, 'w')
        fd.write(jsondata)
        fd.close()
    except:
        print 'ERROR writing', filename
        pass

def put2 (ip, site, filename):
   try:
        jsondata = json.dumps({'ip': ip, 'site':site} )
        fd = open(filename, 'w')
        fd.write(jsondata)
        fd.close()
   except:
        print 'ERROR writing', filename
        pass


if __name__ == "__main__":
    oj = open_json('txt_input.json')
    dictionary = ['dupa', 'kurde', 'kurwa']
    pprint(oj)

    print "Znalezione wyrazy:"
    sw,tt = search_word(oj, dictionary)
    for key, value in sw.items():
       print "%s | count: %s" % (key, value)

    print "Znalezione naglowki:"
    with open ('trial.txt')as fh:
     for line in fh:
      print(get_net_target(line))


    put(tt.__getitem__(0), tt.__getitem__(1),tt.__getitem__(2), sw.items(), 'txt_output.json')
    put2(tt.__getitem__(0),tt.__getitem__(2), 'header_output.json')
