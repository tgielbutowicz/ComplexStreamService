#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ComssServiceDevelopment.connectors.tcp.msg_stream_connector import InputMessageConnector, OutputMessageConnector
from ComssServiceDevelopment.service import Service, ServiceController
import dpkt
import socket


class EndService(Service):
    def run(self):
        while True:
            print self.get_input("testInput").read()

    def declare_inputs(self):
        self.declare_input("testInput", InputMessageConnector(self))

    def declare_outputs(self):
        pass


if __name__=="__main__":
    print "starting"
    sc = ServiceController(EndService, "consumer.json")
    sc.start()