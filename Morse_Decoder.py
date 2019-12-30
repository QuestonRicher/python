import sys
import random

morse_code = {' ':'   ',
              '.-':'A',
              '-...':'B' ,
              '-.-.': 'C',
              '-..': 'D',
              '.':'E',
              '..-.':'F',
              '--.':'G',
              '....':'H',
              '..':'I',
              '.---':'J',
              '-.-':'K',
              '.-..':'L',
              '--':'M',
              '-.':"N",
              '---':'O',
              '.--.':'P',
              '--.-':'Q',
              '.-.':'R',
              '...':'S',
              '-':'T',
              '..-':'U',
              '...-':'V',
              '.--':'W',
              '-..-':'X',
              '-.--':'Y',
              '--..':'Z',}


Sentence = input().upper()

list(Sentence)

print('Message Start ')
len(Sentence)
b = 0
i = 0
j = len(Sentence)


while i < j:
    print(end=' ' + morse_code[Sentence[b]])

    b = b + 1
    i = i + 1
else:
    print('')
    print('Message End')



