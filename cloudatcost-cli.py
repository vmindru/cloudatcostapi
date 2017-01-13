#!/usr/bin/python

import sys
import os
from cloudatcost import cloudatcost

if __name__ == "__main__":
    if os.environ.has_key('CLOUDATCOST_KEY'):
        key = os.environ.get('CLOUDATCOST_KEY')
    else:
        print "Please define bash CLOUDATCOST_KEY var first"
    if os.environ.has_key('CLOUDATCOST_LOGIN'):
        login = os.environ.get('CLOUDATCOST_LOGIN')
    else:
        print "Please define bash CLOUDATCOST_LOGIN var first"
    if len(sys.argv) == 2:
        cl = cloudatcost(key, login)
        cl.request(sys.argv[1])
        print cl.response()
    elif len(sys.argv) > 2:
        cl = cloudatcost(key, login)
        cl.request(sys.argv[1], sys.argv[2:])
        print cl.response()
    else:
        print "input operation"
