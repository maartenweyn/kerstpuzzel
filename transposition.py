import argparse
import sys
import operator
import math
import hunspell

dict = hunspell.HunSpell('/Library/Spelling/nl_NL.dic', '/Library/Spelling/nl_NL.aff')

subst = {}

def decrypt(message, key):
  numOfColumns = math.ceil(len(message) / key)
  numOfRows = key
  numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
  plaintext = [''] * numOfColumns
  col = 0
  row = 0

  for symbol in message:
    plaintext[col] += symbol
    col += 1 # point to next column
    # If there are no more columns OR we're at a shaded box, go back to
    # the first column and the next row.
    if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
      col = 0
      row += 1
    
  return ''.join(plaintext)

def main(argv):
  parser = argparse.ArgumentParser(description='Decode a message hidden by a Transposition cipher.')
  parser.add_argument('cipher')
  args=parser.parse_args()
  cipher=args.cipher

  
  for key in range(2, len(cipher)):
    answer = decrypt(cipher, key)

    words = answer.split()
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

    print('{0:3} ==> {1} {2}'.format(key, answer, indic))
  

if __name__ == "__main__":
   main(sys.argv[1:])
