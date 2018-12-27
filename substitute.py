import argparse
import sys

import hunspell
import random
import itertools

## based on https://inventwithpython.com/hacking/chapter17.html

dict = hunspell.HunSpell('/Library/Spelling/nl_NL.dic', '/Library/Spelling/nl_NL.aff')

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
myKey   = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'

tested_keys = {}

foundkey = False

def getRandomKey():
  key = list(LETTERS)
  random.shuffle(key)
  return ''.join(key)

def checkValidKey(key):
  keyList = list(key)
  lettersList = list(LETTERS)
  keyList.sort()
  lettersList.sort()
  if keyList != lettersList:
    return False
  return True

def substitute(message, key):
  translated = ''
  for c in message:
    if c.isalpha():
      symIndex = key.find(c.upper())
      if c.isupper():
        translated += LETTERS[symIndex].upper()
      else:
        translated += LETTERS[symIndex].lower()
    else:
      translated += c

  words = translated.split()
  indiccount = 0
  for word in words:
  # print the word
    testdict = dict.spell(word)
    if (testdict):
      indiccount += 1
    #print(word, testdict)

  if (indiccount > len(words) * 0.6):
    indic = True
  else:
    indic = False

  print('key: {0} ==> {1} ({2} - {3}/{4})'.format(key, translated, indic, indiccount, len(words)))

  return indic

def main(argv):
  parser = argparse.ArgumentParser(description='Decode a message hidden by a Caesar cipher.')
  parser.add_argument('cipher')
  parser.add_argument('-k', '--key', default='', help='key')
  args=parser.parse_args()
  cipher=args.cipher
  key=args.key

  if key != '':
    print ("Valid key:", checkValidKey(key))
    output = substitute(cipher, key)
  else:

    output = False
    for keytupple in itertools.permutations(LETTERS, len(LETTERS)):
      #print (keytupple)
      key = ''
      for i in keytupple:
        key += i
      #print (key)
      

      #key = getRandomKey()
      #if not key in tested_keys:
      output = substitute(cipher, key)
      if (output):
        tested_keys[key] = output

    print("Found:")
    for key in tested_keys:
      output = substitute(cipher, key)





  


if __name__ == "__main__":
   main(sys.argv[1:])
