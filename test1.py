# taken from PyAudio example of playing wav / callback version
# http://people.csail.mit.edu/hubert/pyaudio/docs/#id4

import pyaudio
import wave
import time

wf = wave.open('shell.wav', 'rb')

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
	data = wf.readframes(frame_count)
	return (data, pyaudio.paContinue)

	
print p.get_format_from_width(wf.getsampwidth())
print pyaudio.paInt16
print wf.getnchannels()

stream = p.open(format = pyaudio.paInt16, 
				channels=wf.getnchannels(),
				rate=wf.getframerate(), 
				frames_per_buffer = 32000,
				output = True, 
				input = False, 
				stream_callback = callback)

#stream = p.open(format = pyaudio.paInt16, 
#				channels = 2, 
#				rate = 44100, 
#				frames_per_buffer = 2048, 
#				output = True, 
#				input = False, 
#				output_device_index = 0, 
#				stream_callback = callback)
				
#stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#				channels=wf.getnchannels(),
#				rate=wf.getframerate(),
#				output=True,
#				stream_callback=callback)

stream.start_stream()

while stream.is_active():
	time.sleep(0.1)

stream.stop_stream()

stream.close()

wf.close()

p.terminate()