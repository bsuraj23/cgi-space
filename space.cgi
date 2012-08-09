#!/usr/bin/env python

from __future__ import division
import os, dstatus

print 'Content-Type: text/html\n'

print '<html><head><title>Disk Status</title></head>'
print '<body><h1>Disk  Status</h1>'
if os.name == 'posix':
    for dmount in dstatus.getdlist():
        dinfo = dstatus.getdinfo(dmount)
        dstatus.printdstat(dmount,dstatus.gettdsize(dinfo),dstatus.getfdsize(dinfo),dstatus.getudsize(dinfo))
else:
    print '<p>Error: This script works on Linux only!</p>'
print '</body></html>'
