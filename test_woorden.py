import argparse
import sys

import hunspell
import random
import itertools

dict = hunspell.HunSpell('/Library/Spelling/nl_NL.dic', '/Library/Spelling/nl_NL.aff')


woorden = {"PART"}
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

antwoord = []


def main(argv):

  for c in LETTERS:
    #print(c)
    bestaat = True
    antwoord = []
    for woord in woorden:
      woordok = False
      test_woord = c + woord
      for new_word_tupple in itertools.permutations(test_woord):
        new_word = ''.join(new_word_tupple)
        #print (new_word, dict.spell(new_word))
        newwoordok = dict.spell(new_word)
      # for i in range(len(woord)):
      #   new_word = woord[:i] + c + woord[i:]
        
        if newwoordok:
          woordok = True
          antwoord.append(new_word)
          #print("{0} : {1} {2}".format(i, new_word, newwoordok))
          #print("{0} {1}".format(new_word, newwoordok))

      if not woordok:
        bestaat = False
    
    if bestaat:
      print("Gevonden: ", c, antwoord)



  


if __name__ == "__main__":
  main(sys.argv[1:])