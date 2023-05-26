#!/usr/bin/env python3

import re

from scapy.all import *

class P4calc(Packet):
    name = "P4calc"
    fields_desc = [ StrFixedLenField("P", "P", length=1),
                    StrFixedLenField("Four", "4", length=1),
                    XByteField("version", 0x01),
                    #StrFixedLenField("order", "+", length=3),
                    XByteField("order", 0),
                    #IntField("order", 0),
                    IntField("bid_price", 10),
                    IntField("ask_price", 100),
                    IntField("result", 404)]

bind_layers(Ether, P4calc, type=0x1234)

class NumParseError(Exception):
    pass

class OpParseError(Exception):
    pass

class Token:
    def __init__(self,type,value = None):
        self.type = type
        self.value = value



def get_if():
    ifs=get_if_list()
    iface= "veth0-1" # "h1-eth0"
    #for i in get_if_list():
    #    if "eth0" in i:
    #        iface=i
    #        break;
    #if not iface:
    #    print("Cannot find eth0 interface")
    #    exit(1)
    #print(iface)
    return iface


def randomOrder():
    action_list = [0, 1] # bid: 0, ask: 1
    return random.choice(action_list)


def main():

    #order=1
    num_orders = 10

    
    s = ''
    #iface = get_if()
    #iface = "veth0-1"
    iface = "enx0c37965f89ec"

    for i in range(num_orders):
        order = randomOrder()
        """
        s = input('> ')
        if s == "quit":
            break
        print(s) 
        """
        try:
            pkt = Ether(dst='00:04:00:00:00:00', type=0x1234) / P4calc(order=order,
                                              bid_price=8,
                                              ask_price=98)
            pkt = pkt/' '

            #pkt.show()
            resp = srp1(pkt, iface=iface,timeout=5, verbose=False)
            
            if resp:
                p4calc=resp[P4calc]
                if p4calc:
                    print(p4calc.result)
                else:
                    print("cannot find P4calc header in the packet")
            else:
                print("Didn't receive response")
        except Exception as error:
            print(error)


if __name__ == '__main__':
    main()


