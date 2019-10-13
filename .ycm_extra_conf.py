# -Os -g -std=gnu99 -Wall -funsigned-char -funsigned-bitfields -fpack-struct -fshort-enums  -ffunction-sections -fdata-sections  -DF_CPU=1000000UL -DBAUD=9600UL -I. -I../../AVR-Programming-Library -mmcu=atmega328p -c -o stoplight.o stoplight.c
def Settings( **kwargs ):
  return {
    'flags': [ '-Os', '-g', '-std=gnu99', '-Wall', '-funsigned-char',
'-D__AVR_ATmega328P__',
      '-isystem','/usr/lib/avr/include/avr/',
'-funsigned-char',
'-fpack-struct',
'-fshort-enums',
     '-funsigned-bitfields', '-fpack-struct', '-fshort-enums',
     '-ffunction-sections', '-fdata-sections',
'-Wall',
'-Wstrict-prototypes',
      '-isystem /usr/lib/avr/include/avr/',
      '-isystem/usr/lib/avr/include/avr/',
      '-I','/usr/lib/avr/include/avr/',
      '-isystem','/usr/lib/avr/include/',
      '-isystem','/usr/lib/avr/include/',
      '-I/usr/lib/avr/include/',
     '-funsigned-bitfields', '-fpack-struct', '-fshort-enums',
     '-ffunction-sections', '-fdata-sections',
     '-DF_CPU=1000000UL',
     '-DBAUD=9600UL',
     '-I.', '-I../../AVR-Programming-Library',
     '-mmcu=atmega328p',
     '-c'
     ]
  }

