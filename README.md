# Magic Trout Imaginarium

Main executable is Kilgore.py  

Audio is wav format and should be at 48K native or stuttering occur.  

The following is also documented in Kilgore.py  

GPIO for motor control uses Physical Numbering  

The tail and mouth are both just on/off but the head is controlled with a bidirectional h-bridge. The head can be driven both forward and backward. The tail and mouth are returned by spring.

Tail Head0 Head1 Mouth    
Physical pinout:  11, 15, 16, 18  
GPIO pinout: 17, 22, 23, 24  

-----------------------------------  
#### Wiring (physical pins)
- 01 *3.3V
- 02 5V
- 03 BCM2(SDA)
- 04 5V
- 05 BCM3(SCL)
- 06 GRND
- 07 BCM4(GPCLK0)
- 08 BCM14
- 09 GRND
- 10 BCM15
- 11 *BCM17 TAIL
- 12 BCM18
- 13 BCM27
- 14 GRND
- 15 *BCM22 HEAD0
- 16 *BCM23 HEAD1
- 17 3.3V
- 18 *BCM24 MOUTH
- 19 BCM10(MOSI)
- 20 *GRND


Example video of operation  
https://www.youtube.com/watch?v=7busGsuIOU4  
