#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ComssServiceDevelopment.connectors.tcp.msg_stream_connector import InputMessageConnector, OutputMessageConnector
from ComssServiceDevelopment.service import Service, ServiceController
import dpkt
import socket


class TCP_Reassembler(Service):
    def run(self):
        output = self.get_output("tcpOutput")
        while True:
            buf = self.get_input("tcpInput").read()

            output.send(str(buf))

    def declare_inputs(self):
        self.declare_input("tcpInput", InputMessageConnector(self))

    def declare_outputs(self):
        self.declare_output("tcpOutput", OutputMessageConnector(self))


if __name__=="__main__":
    sc = ServiceController(TCP_Reassembler, "tcp_reassembler.json")
    sc.start()
