'slight variant on yours:
 _xinfreq = 5_000_000
  _clkmode = xtal1 + pll16x


CON

  hc0 = 16
  hc1 = 17

  pin =  15      ' red = 4, green = 3, blue = 2

  range = 100
  rate = 200_000

  motorDelay = 4_500_000

PUB LedOnOff | duty

  dira[hc0] :=1
  dira[hc1] :=1
     

  repeat

    outa[hc0] := 1
    outa[hc1] := 0
    
    waitcnt(motorDelay + cnt)     '  Wait for Delay cycles
    waitcnt(motorDelay + cnt)     '  Wait for Delay cycles
    waitcnt(motorDelay + cnt)     '  Wait for Delay cycles
     
    outa[hc0] := 1
    outa[hc1] := 1
     
    waitcnt(motorDelay + cnt)     '  Wait for Delay cycles
    waitcnt(motorDelay + cnt)     '  Wait for Delay cycles
    waitcnt(motorDelay + cnt)     '  Wait for Delay cycles
     
    outa[hc0] := 0
    outa[hc1] := 1
     
    waitcnt(motorDelay + cnt)     '  Wait for Delay cycles
     
    outa[hc0] := 0
    outa[hc1] := 0

    waitcnt(motorDelay + cnt)     '  Wait for Delay cycles
    waitcnt(motorDelay + cnt)     '  Wait for Delay cycles
    waitcnt(motorDelay + cnt)     '  Wait for Delay cycles
     
