__author__ = 'Sandra'



#!/usr/bin/env python

import dpkt


f = open(r'C:/Users/Sandra/PycharmProjects/ComplexStreamService/http_page_splitter/test.pcap')

pcap = dpkt.pcap.Reader(f)

for ts, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    tcp = ip.data

    if tcp.dport == 80 and len(tcp.data) > 0:
        http = dpkt.http.Request(tcp.data)
        print http.uri

f.close()