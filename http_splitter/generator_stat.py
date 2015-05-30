__author__ = 'Sandra'
import sys
import json
import re
from pprint import pprint
from collections import Counter
from collections import defaultdict

ip_file = open("stats.json",'w')

count_unique_IP = sum(1 for line in set(open('header_output.json')))
print count_unique_IP

with open('header_output.json') as f:
    lines = sorted(set(line.strip('\n') for line in f))
for line in lines:
    print line
    ip_file.write(line)
    ip_file.close


