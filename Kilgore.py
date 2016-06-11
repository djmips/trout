# Kilgore Trout

#-- Tools --
# Location
#/home/pi/trout
# Terminal
#H:\DROPBOX\Dropbox\DEV\RaspPi\putty 
#username: pi
#password: raspberry
# Transfer files (same login)
#D:\Program Files (x86)\FileZilla FTP Client\filezilla.exe
# Test audio
#aplay file.wav

#-- Hardware GPIO --
# 7 -> LED 
# 8,9 Mouth
# 10,11 Turn
# 12,13 Tail

# Power
# Need 3Amp power hooked up to micro USB + motors + Audio amp / speakers

import signal
import sys
import os
import pyaudio
import RPi.GPIO as GPIO
import time

#-- Data --
# array of wav sounds

#-- Code --

#subroutines


def signal_handler(signal, frame):
	print 'You pressed Ctrl+C!'
	GPIO.output(11, False)
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

#

class Timer:
	#
	function = time.clock

	# is providing a start time
	@staticmethod
	def value():
		return Timer.function()

	# calculating delta between current time and start time.
	@staticmethod
	def delta(start):
		return Timer.function() - start


#test

GPIO.setup(11, GPIO.OUT)
GPIO.output(11, False)


while True:
	GPIO.output(11,True)
	time.sleep(0.5)
	GPIO.output(11,False)
	time.sleep(0.5)

#Wait for button press

#Pick random audio sound from array

# load audio into memory 48K wave file

# Create Generator for Tail flap
# Create Generator for Turn control
# Create Generator for mouth lip sync - pass in audio raw data

# start audio playing

#  update tail flap
#  update turn control
#  update lip sync

# until audio finished

# return fish to neutral

# To top of program
