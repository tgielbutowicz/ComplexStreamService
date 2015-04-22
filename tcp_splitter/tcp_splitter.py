#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ComssServiceDevelopment.connectors.udp.multicast import InputMulticastConnector
from ComssServiceDevelopment.connectors.tcp.msg_stream_connector import InputMessageConnector, OutputMessageConnector
from ComssServiceDevelopment.service import Service, ServiceController
import dpkt
import socket


class TCP_Splitter(Service):
    def run(self):
        output = self.get_output("tcpOutput")
        while True:
            buf = self.get_input("pcapInput").read()
            e = dpkt.ethernet.Ethernet(buf)
            if e.type!=dpkt.ethernet.ETH_TYPE_IP:
                continue
            ip=e.data
            if ip.p not in (dpkt.ip.IP_PROTO_TCP, dpkt.ip.IP_PROTO_UDP):
                continue
            tcp=ip.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print "%s -> %s" % (src, dst)
            print "port: %s -> %s" % (tcp.sport, tcp.dport)
            output.send(str(tcp))

    def declare_inputs(self):
        self.declare_input("pcapInput", InputMulticastConnector(self))

    def declare_outputs(self):
        self.declare_output("tcpOutput", OutputMessageConnector(self))


if __name__=="__main__":
    sc = ServiceController(TCP_Splitter, "tcp_splitter.json")
    sc.start()
