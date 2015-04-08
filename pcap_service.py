#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ComssServiceDevelopment.connectors.udp.multicast import InputMulticastConnector
from ComssServiceDevelopment.service import Service, ServiceController


class PcapService(Service):
    def run(self):
        while True:
            print self.get_input("pcapInput").read()

    def declare_inputs(self):
        self.declare_input("pcapInput", InputMulticastConnector(self))

    def declare_outputs(self):
        pass


if __name__=="__main__":
    sc = ServiceController(PcapService, "pcap_service.json")
    sc.start()

#mmmm test