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

#-- Defines --

TAIL = 0
HEAD0 = 1
HEAD1 = 2
MOUTH = 3

#-- Data --
# array of wav sounds
pins = [11, 15, 16, 18]

#-- Code --

#classes

class ProfileTimer:
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

		
class Timer:
	#
	function = time.time

	# is providing a start time
	@staticmethod
	def value():
		return Timer.function()

	# calculating delta between current time and start time.
	@staticmethod
	def delta(start):
		return Timer.function() - start		
		
#subroutines

def test_fish():
	start = Timer.value();
	while Timer.delta(start) < 10.0:
		#print Timer.delta(start)
		#for n in pins:
			#GPIO.output(n, True)
		GPIO.output(pins[HEAD0], True)
		GPIO.output(pins[HEAD1], False)
		time.sleep(0.9)
		#for n in pins:
			#GPIO.output(n, False)
		GPIO.output(pins[HEAD0], False)
		GPIO.output(pins[HEAD1], True)
		time.sleep(0.5)

def signal_handler(signal, frame):
	print 'You pressed Ctrl+C!'
	for n in pins:
		GPIO.output(n, False)
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

#

# setup the pins as output 
for n in pins:
	GPIO.setup(n, GPIO.OUT)
	GPIO.output(n, False)

test_fish();

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
