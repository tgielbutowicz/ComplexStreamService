#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssServiceDevelopment.connectors.udp.multicast import OutputMulticastConnector
from ComssServiceDevelopment.development import DevServiceController
import dpkt
import time
import sys

service_controller = DevServiceController("pcap_service.json")
service_controller.declare_connection("pcapInput", OutputMulticastConnector(service_controller))

class P():
    def __init__(self,ts,buf):
        self.ts=ts
        self.buf=buf

def open_pcap(file_name):
    f = open(file_name,"rb") #works only in binary mode
    p = dpkt.pcap.Reader(f)
    return p

def packetizer(p):
    for ts, buf in p:
        #print pickle.dumps(buf)
        #e = dpkt.ethernet.Ethernet(buf)
        #print "%x" % e.type
        #print "IP src: %s" % e.data.src
        yield (ts,buf)
        #print ts, len(buf)
        #e = dpkt.ethernet.Ethernet(buf)
        ##print e.data
        ##print "+++++++++++++++++++++"
        #yield (ts,str(e))

if __name__ == "__main__":
    print "Opening file: %s" % sys.argv[1]
    p = open_pcap(sys.argv[1])
    for ts,data in packetizer(p):
        service_controller.get_connection("pcapInput").send(data)
        time.sleep(1)
    service_controller.get_connection("pcapInput").close()