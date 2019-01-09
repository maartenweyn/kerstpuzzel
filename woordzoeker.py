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

def print_result(result, columns, rows):
  combined = [['.' for x in range(columns)] for y in range(rows)]

  for direction in result:
    print (direction)
    for i, row in enumerate(result[direction]):
      col = ''
      for j, e in enumerate(row):
        col += e + " "
        if e is not '.':
          combined[i][j] = e
      print(col)

  print("combined:")
  for row in combined:
    col = ''
    for e in row:
      col += e + " "
    print(col)

def search_words(puzzle):
  wordgrid = puzzle.replace(' ','').lower()
  if len(wordgrid)-1 is not '\n':
    wordgrid += '\n'
  length = wordgrid.index('\n')+1
  columns = wordgrid.index('\n')
  rows = wordgrid.count('\n')
  results  = {}

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

  antwoord = {}

  for direction, tuple in wordlines.items():
      #print (direction)
      
      results[direction] = [['.' for x in range(columns)] for y in range(rows)]



      text = ''
      tuples = []
      for t in tuple:
        if t[0] is not "\n":
          text += t[0] 
          tuples.append(t)
        else:
          #print ("text", text, len(text))
          words = []
          #list of all words
          for start in range(len(text)-1):
            for stop in range(len(text), start+2, -1):
              #print(start, stop, stop - start, text[start:stop])
              words.append([text[start:stop], stop - start, start, stop])

          words = sorted(words, key=lambda x: x[1], reverse=True)
          for word in words:
            #print (word)
            if (dict.spell(word[0])):
              #print ("dict", word)
              if word[0] not in antwoord:
                antwoord[word[0]] = [tuples[word[2]][1][0], tuples[word[2]][1][1]]
                for j in range(word[2], word[3]):
                  #print("tuples", tuples[j][0], tuples[j][1][0], tuples[j][1][1])
                  results[direction][tuples[j][1][0]][tuples[j][1][1]] = tuples[j][0]
                      
                    #print("F: {0} ({1},{2}) [{3}]".format(words[:i], index, lijn, len(words[:i])))
                    #start += (i - start)

                break

          text = ''
          tuples = []

  print(antwoord)
  print_result(results, columns, rows)

  return antwoord, results

def main(argv):
  parser = argparse.ArgumentParser(description='Decode a message hidden by a vigenere cipher.')
  parser.add_argument('cipher')

  args=parser.parse_args()
  cipher=args.cipher.lower()

  search_words(cipher)


if __name__ == "__main__":
  #search_words(puzzle)
  main(sys.argv[1:])