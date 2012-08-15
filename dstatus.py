#!/usr/bin/env python

from __future__ import division
import os, commands

def getdlist(): #linux only
    dstring = commands.getoutput("cat /proc/mounts | gawk '{ print $2 }'")#list of mounted disks, like ['/', '/proc', '/sys', '/dev/pts']
    dlist = dstring.split('\n')
    return dlist

def getdinfo(dmount):
    dinfo = os.statvfs(dmount)
    return dinfo

def gettdsize(dinfo):
    tdsize =  dinfo[0] *  dinfo[2] / 1024 / 1024 / 1024 #total disk size in GB
    return tdsize

def getfdsize(dinfo):
    fdsize = dinfo[0] * dinfo[4] / 1024 / 1024 / 1024 #free disk size in GB
    return fdsize

def getudsize(dinfo):
    udsize = dinfo[0] * ( dinfo[2] - dinfo[4] ) / 1024 / 1024 / 1024 #used disk size in GB
    return udsize

def printdstat(dmount,tdsize,fdsize,udsize):
    if (tdsize != 0 ):
        print '<article><h2>%s</h2>' %dmount
        print '<strong>Free Disk Space: %5.2fGB</strong>' %fdsize
        print '<br>Total Disk Space: %5.2fGB' %tdsize
        print '<br> <progress value="%s" max="%s"></progress><br>' %(udsize, tdsize)
        print '</article>'
