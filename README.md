# integersto7segmentusinglist

seven-segment display.

It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. 

program converts a integer number to a seven-display device, although we're going to use single LEDs instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:

for example: 
input is 123

output is
  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 
