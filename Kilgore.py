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
import RPi.GPIO as GPIO
import time
import wave
import getopt
import alsaaudio
import random


#-- Defines --

#input BCM
BUTTON = 18

#output index
TAIL = 0
HEAD0 = 1
HEAD1 = 2
MOUTH = 3

#-- Data --

# GPIO for motor control uses Physical Numbering
#   TAIL HEAD0 HEAD1 MOUTH
# pin   11, 15, 16, 18
pins = [17, 22, 23, 24]

#01 [ *3.3V          5V            ]
#03 [  BCM2(SDA)     5V            ]
#05 [  BCM3(SCL)     GRND          ]
#07 [  BCM4(GPCLK0)  BCM14         ]
#09 [  GRND          BCM15         ]
#11 [ *BCM17 TAIL    BCM18         ]
#13 [  BCM27         GRND          ]
#15 [ *BCM22 HEAD0  *BCM23 HEAD1   ]
#17 [  3.3V         *BCM24 MOUTH   ]
#19 [  BCM10(MOSI)  *GRND          ]

# array of fortune wav sounds
fortunes = ['03','05','06','07','10','12','14','16','17','18','19','21','22','26','27','32']
# 30 is special and is the welcome to the imaginarium line

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

def setSampWidth(f):
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

		
def headUp():
	print "headUp"
	GPIO.output(pins[HEAD0], True)
	#PIO.output(pins[HEAD1], False)	
		
def headDown():
	print "headDown"
	GPIO.output(pins[HEAD0], False)
	GPIO.output(pins[HEAD1], True)

def tailStart():
	print "tailStart"
	GPIO.output(pins[TAIL], True)
	
def tailStop():
	print "tailStop"
	GPIO.output(pins[TAIL], False)

def mouthStart():
	print "mouthStart"
	GPIO.output(pins[MOUTH], True)
	
def mouthStop():
	print "mouthStop"
	GPIO.output(pins[MOUTH], False)
	
	
def headMove():
	a = 1
	while (a < 10000):
		headUp()

		s1 = Timer.value();
		while Timer.delta(s1) < 2.9:
			yield a
		
		headDown()

		s2 = Timer.value();
		while Timer.delta(s2) < 3.0:
			#print "foooo" + str(Timer.delta(s2))
			yield a
			
		yield a


def tailFlap():
	#print Timer.delta(start)
	a = 1
	while (a < 10000):
		tailStart()

		s1 = Timer.value();
		while Timer.delta(s1) < 0.4:
			yield a
		
		tailStop()

		s2 = Timer.value();
		while Timer.delta(s2) < 0.4:
			yield a
			
		yield a
		
def mouthFlap():
	#print Timer.delta(start)
	a = 1
	while (a < 10000):
		mouthStart()

		s1 = Timer.value();
		while Timer.delta(s1) < 0.2:
			yield a
		
		mouthStop()

		s2 = Timer.value();
		while Timer.delta(s2) < 0.3:
			yield a
			
		yield a
		
		
def resetPins():
	for n in pins:
		GPIO.output(n, False)		
		
def signal_handler(signal, frame):
	print 'You pressed Ctrl+C!'
	resetPins()
	sys.exit(0)


#START #####################################################################

signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # for push button 

# setup the pins as output 
for n in pins:
	GPIO.setup(n, GPIO.OUT)
	GPIO.output(n, False)
	
device = alsaaudio.PCM()
card = 'default'

head = headMove()
tail = tailFlap()
mouth = mouthFlap()	

while True:

	button_pressed = False
	
	t0 = Timer.value()
	while Timer.delta(t0) < 300.0:
		input_state = GPIO.input(BUTTON)
		if input_state == False:
			button_pressed = True
			print('Button Pressed')
			break

			
	print "START -------"
	t0 = Timer.value()
	while Timer.delta(t0) < 0.1:
		pass
		
	head = headMove()
	tail = tailFlap()
	mouth = mouthFlap()	
		  
	if (button_pressed == True):
		fortune_pick = random.choice(fortunes)
		fortuneFile = "/home/pi/trout/wave/Recording" + fortune_pick + ".wav"
	else:
		fortuneFile = "/home/pi/trout/wave/Recording" + "30" + ".wav"
		
	print fortuneFile
	   
	f = wave.open( fortuneFile, 'rb')

	device = alsaaudio.PCM()
	
	mixer = alsaaudio.Mixer('PCM')
	mixer.setvolume(95)

	# Set attributes
	print f.getnchannels()
	device.setchannels(f.getnchannels())
	device.setrate(f.getframerate())
	setSampWidth(f)
	device.setperiodsize(320)   
	data = f.readframes(320)

	# tail flap starts it
	t0 = Timer.value()
	while Timer.delta(t0) < 4.0:
		b = tail.next()

	# head forward still tail flapping
	headUp()
	t0 = Timer.value()
	while Timer.delta(t0) < 1.0:
		b = tail.next()

	# play audio with lip flap	
	while data:
		# Read data from stdin
		a = 1
		device.write(data)
		data = f.readframes(320)
		a = head.next()
		b = tail.next()
		c = mouth.next()

	mouthStop()
		
	#but continue to flap tail without mouth flap	
	t0 = Timer.value()
	while Timer.delta(t0) < 2.0:
		b = tail.next()
		
	headDown()
		
	#but continue to flap tail for a few seconds	
	t0 = Timer.value()
	while Timer.delta(t0) < 2.0:
		b = tail.next()

	tailStop()
		
	t0 = Timer.value()
	while Timer.delta(t0) < 2.5:
		pass
		
	resetPins()

	print "close file"
	f.close()	

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
