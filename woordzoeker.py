import argparse
import sys

import hunspell

dict = hunspell.HunSpell('/Library/Spelling/nl_NL.dic', '/Library/Spelling/nl_NL.aff')

puzzle ='''SAHAHWPHEWY
XZQRNIWMXNZ
KYHVQRJWUYU
DPOXWWTDVYU
SCQXLNKIBHL
YAKVUMDDGHM
UAQZIMBQDGU
JOZRKLNGROF
GJRNQMSMZOJ
IVBBVINJJTS
VSONETPZWPG'''

wordgrid = puzzle.replace(' ','').lower()
length = wordgrid.index('\n')+1
characters = [(letter, divmod(index, length))
            for  index, letter in enumerate (wordgrid)]

wordlines = {}
# These next lines just  directions so you can tell which direction the word is going
directions = {'going downwards':0, 'going downwards and left diagonally':-1, 'going downwards and right diagonally':1}

for word_direction, directions in directions.items():
    wordlines[word_direction] = []
    for x in range(length):
        for i in range(x, len(characters), length + directions):
            wordlines[word_direction].append(characters[i])
        wordlines[word_direction].append('\n')

# Nice neat way of doing reversed directions.
wordlines['going right'] = characters
wordlines['going left'] = [i for i in reversed(characters)]
wordlines['going upwards'] = [i for i in reversed(wordlines['going downwards'])]
wordlines['going upwards and left diagonally'] = [i for i in reversed(wordlines['going downwards and right diagonally'])]
wordlines['going upwards and right diagonally'] = [i for i in reversed(wordlines['going downwards and left diagonally'])]

for direction, tuple in wordlines.items():
    string = ''.join([i[0] for i in tuple])
    #string = string.strip()
    print (direction)
    #print (direction, string.split())

    antwoord = {}
    
    lijn = 0
    for line in string.split():
      index = 1
      lijn += 1
      start = 0
      #print (string, len(words))

      #STARTING FROM FRONT
      words = line
      while len(words) >= 3:
        wordFound = False
        #print (words, len(words))
        for i in range(len(words), 2, -1):
          #print("testing {0} at {1} to {2}".format(words[:i], start, i))
          if (len(words[:i]) > 3):
            if (dict.spell(words[:i])):
              if words[:i] not in antwoord:
                antwoord[words[:i]] = [index, lijn, len(words[:i])]
                #print("F: {0} ({1},{2}) [{3}]".format(words[:i], index, lijn, len(words[:i])))
                #start += (i - start)
              index += len(words[:i])
              words = words[i:]
              wordFound = True
              break
        if (not wordFound):
          words = words[1:]
          index += 1

      #STARTING FROM BACK
      words = line
      while len(words) >= 3:
        wordFound = False
        #print (words, len(words))
        for i in range(len(words)-1):
          #print("testing {0} at {1} to {2}".format(words[:i], start, i))
          if (len(words[i:]) > 3):
            if (dict.spell(words[i:])):
              if words[:i] not in antwoord:
                antwoord[words[:i]] = [index, lijn, len(words[i:])]
                #print("B: {0} ({1},{2}) [{3}]".format(words[i:], index, lijn, len(words[i:])))
              #start += (i - start)
              index += len(words[i:])
              words = words[:i]
              wordFound = True
              break
        if (not wordFound):
          words = words[:-1]
          index += 1

    print (antwoord)
