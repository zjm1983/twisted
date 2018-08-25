# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

#

import tty

# this module was autogenerated.

VINTR = 1
VQUIT = 2
VERASE = 3
VKILL = 4
VEOF = 5
VEOL = 6
VEOL2 = 7
VSTART = 8
VSTOP = 9
VSUSP = 10
VDSUSP = 11
VREPRINT = 12
VWERASE = 13
VLNEXT = 14
VFLUSH = 15
VSWTCH = 16
VSTATUS = 17
VDISCARD = 18
IGNPAR = 30
PARMRK = 31
INPCK = 32
ISTRIP = 33
INLCR = 34
IGNCR = 35
ICRNL = 36
IUCLC = 37
IXON = 38
IXANY = 39
IXOFF = 40
IMAXBEL = 41
ISIG = 50
ICANON = 51
XCASE = 52
ECHO = 53
ECHOE = 54
ECHOK = 55
ECHONL = 56
NOFLSH = 57
TOSTOP = 58
IEXTEN = 59
ECHOCTL = 60
ECHOKE = 61
PENDIN = 62
OPOST = 70
OLCUC = 71
ONLCR = 72
OCRNL = 73
ONOCR = 74
ONLRET = 75
CS7 = 90
CS8 = 91
PARENB = 92
PARODD = 93
TTY_OP_ISPEED = 128
TTY_OP_OSPEED = 129

TTYMODES = {
    1: 'VINTR',
    2: 'VQUIT',
    3: 'VERASE',
    4: 'VKILL',
    5: 'VEOF',
    6: 'VEOL',
    7: 'VEOL2',
    8: 'VSTART',
    9: 'VSTOP',
    10: 'VSUSP',
    11: 'VDSUSP',
    12: 'VREPRINT',
    13: 'VWERASE',
    14: 'VLNEXT',
    15: 'VFLUSH',
    16: 'VSWTCH',
    17: 'VSTATUS',
    18: 'VDISCARD',
    30: (tty.IFLAG, 'IGNPAR'),
    31: (tty.IFLAG, 'PARMRK'),
    32: (tty.IFLAG, 'INPCK'),
    33: (tty.IFLAG, 'ISTRIP'),
    34: (tty.IFLAG, 'INLCR'),
    35: (tty.IFLAG, 'IGNCR'),
    36: (tty.IFLAG, 'ICRNL'),
    37: (tty.IFLAG, 'IUCLC'),
    38: (tty.IFLAG, 'IXON'),
    39: (tty.IFLAG, 'IXANY'),
    40: (tty.IFLAG, 'IXOFF'),
    41: (tty.IFLAG, 'IMAXBEL'),
    50: (tty.LFLAG, 'ISIG'),
    51: (tty.LFLAG, 'ICANON'),
    52: (tty.LFLAG, 'XCASE'),
    53: (tty.LFLAG, 'ECHO'),
    54: (tty.LFLAG, 'ECHOE'),
    55: (tty.LFLAG, 'ECHOK'),
    56: (tty.LFLAG, 'ECHONL'),
    57: (tty.LFLAG, 'NOFLSH'),
    58: (tty.LFLAG, 'TOSTOP'),
    59: (tty.LFLAG, 'IEXTEN'),
    60: (tty.LFLAG, 'ECHOCTL'),
    61: (tty.LFLAG, 'ECHOKE'),
    62: (tty.LFLAG, 'PENDIN'),
    70: (tty.OFLAG, 'OPOST'),
    71: (tty.OFLAG, 'OLCUC'),
    72: (tty.OFLAG, 'ONLCR'),
    73: (tty.OFLAG, 'OCRNL'),
    74: (tty.OFLAG, 'ONOCR'),
    75: (tty.OFLAG, 'ONLRET'),
    #   90 : (tty.CFLAG, 'CS7'),
    #   91 : (tty.CFLAG, 'CS8'),
    92: (tty.CFLAG, 'PARENB'),
    93: (tty.CFLAG, 'PARODD'),
    128: 'ISPEED',
    129: 'OSPEED',
}
