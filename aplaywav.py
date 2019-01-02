#!/usr/bin/env python

# Simple test script that plays (some) wav files

from __future__ import print_function

import sys
import wave
import getopt
import alsaaudio

def play(device, f):    

    print('%d channels, %d sampling rate\n' % (f.getnchannels(),
                                               f.getframerate()))
    # Set attributes
    device.setchannels(f.getnchannels())
    device.setrate(f.getframerate())

    # 8bit is unsigned in wav files
    if f.getsampwidth() == 1:
        device.setformat(alsaaudio.PCM_FORMAT_U8)
    # Otherwise we assume signed data, little endian
    elif f.getsampwidth() == 2:
        device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    elif f.getsampwidth() == 3:
        device.setformat(alsaaudio.PCM_FORMAT_S24_LE)
    elif f.getsampwidth() == 4:
        device.setformat(alsaaudio.PCM_FORMAT_S32_LE)
    else:
        raise ValueError('Unsupported format')

    device.setperiodsize(320)
    
    data = f.readframes(320)
    while data:
        # Read data from stdin
        device.write(data)
        data = f.readframes(320)


def usage():
    print('usage: aplaywav.py [-c <card>] <file>', file=sys.stderr)
    sys.exit(2)

if __name__ == '__main__':

    card = 'default'

    opts, args = getopt.getopt(sys.argv[1:], 'c:')
    for o, a in opts:
        if o == '-c':
            card = a

    if not args:
        usage()
        
    f = wave.open(args[0], 'rb')
    #device = alsaaudio.PCM(card=card)
    device = alsaaudio.PCM()

    play(device, f)

    f.close()
