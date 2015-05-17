__author__ = 'Sandra'
import sys
import re



def get_word(page):
    start_link=page.find("ip:")
    start_quote=page.find('"',start_link)
    end_quote=page.find('"',start_quote+1)
    word=page[start_quote+1:end_quote]

    return word

def get_word2(page):
    start_link=page.find("port:")
    start_quote=page.find('"',start_link)
    end_quote=page.find('"',start_quote+1)
    word2=page[start_quote+1:end_quote]

    return word2



def get_net_target(page):
    start_link=page.find("href")
    start_quote=page.find('"',start_link)
    end_quote=page.find('"',start_quote+1)
    url=page[start_quote+1:end_quote]

    return url



with open("trial.txt") as fh:
   for line in fh:
      print(get_net_target(line),get_word(line),get_word2(line))






