''This code example is from Propeller Education Kit Labs: Fundamentals, v1.1.
''A .pdf copy of the book is available from www.parallax.com, and also through
''the Propeller Tool software's Help menu (v1.2.6 or newer).
''
''File: LedsOnOff.spin
''All LEDS on for 1/4 s and off ''for 3/4 s.

OBJ
    ser : "FullDuplexSerial"
    
PUB BlinkLeds

    ser.start(31,30,0,19200)
    'wait for any input from terminal
    ser.rx  
    ser.str(STRING("Starting Up",13))

    dira[8] := %1

    repeat

        outa[8] := %1
        waitcnt(clkfreq/4 + cnt)
        outa[8] := %0
        waitcnt(clkfreq/4*3 + cnt)