{{Output.spin
Toggle two pins, simultaneously.}}

  _xinfreq = 5_000_000
  _clkmode = xtal1 + pll1x
  
VAR
  long  Stack[9]             'Stack space for new cog

PUB Main
  cognew(Toggle(8, 3_000_000, 50), @Stack)     'Toggle P16 ten times, 1/4 s each
  Toggle(9, 2_000_000, 20)                     'Toggle P17 twenty times, 1/6 s each

PUB Toggle(Pin, Delay, Count)
{{Toggle Pin, Count times with Delay clock cycles in between.}}

  dira[Pin]~~                'Set I/O pin to output direction
  repeat Count               'Repeat for Count iterations
    !outa[Pin]               '  Toggle I/O Pin
    waitcnt(Delay + cnt)     '  Wait for Delay cycles