import argparse
import sys

import itertools

import hunspell

import multiprocessing
from multiprocessing import Pool
from functools import partial


dict = hunspell.HunSpell('/Library/Spelling/nl_NL.dic', '/Library/Spelling/nl_NL.aff')


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def search_words(text):
  #list of all words
  start = 0

  count = 0
  words = []
  while start < len(text) - 2:
    wordFound = False
    for stop in range(len(text), start+2, -1):
      #print(start, stop, stop - start, text[start:stop])
      word = text[start:stop]

    
      #print (word)
      if (dict.spell(word)):
        #print ("dict", word)
        count += len(word)
        start = stop + 1
        wordFound = True
        words.append(word)
        break

    if not wordFound:
      start += 1

  return count, words


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

  #print('key: {0} ==> {1} ({2} - {3}/{4})'.format(key, translated, indic, indiccount, len(words)))

  return translated


def test_tupple(cipher, keytupple):
  #print (keytupple)
  key = ''
  for i in keytupple:
    key += i
  #print (key)
  
  #if not key in tested_keys:
  output = substitute(cipher, key)
  count, words = search_words(output)

  return count, output, key, words

def main(argv):
  parser = argparse.ArgumentParser(description='Test substitution in woordzoeker')
  parser.add_argument('cipher')
  args=parser.parse_args()
  cipher=args.cipher

  cipher=cipher.lower()

  best_results = []

  func = partial(test_tupple, cipher)
  with multiprocessing.Pool() as pool: # default is optimal number of processes
    for count, output, key, words in pool.imap_unordered(func, itertools.permutations(LETTERS, len(LETTERS))):
      if len(best_results) <= 50:
        best_results.append([count, output, key, words])
        print('{0} ==> {1} ({2}) {3}'.format(count, output, key, words))
      else:
        if count > best_results[50][0]:
          best_results[50] = [count, output, key, words]
          print('{0} ==> {1} ({2}) {3}'.format(count, output, key, words))

      best_results = sorted(best_results, key=lambda x: x[1], reverse=True)

    


  # for keytupple in itertools.permutations(LETTERS, len(LETTERS)):
    # #print (keytupple)
    # key = ''
    # for i in keytupple:
    #   key += i
    # #print (key)
    
    # #if not key in tested_keys:
    # output = substitute(cipher, key)
    # count, words = search_words(output)

    # if len(best_results) <= 50:
    #   best_results.append([count, output, key, words])
    #   print('{0} ==> {1} ({2}) {3}'.format(count, output, key, words))
    # else:
    #   if count > best_results[50][0]:
    #     best_results[50] = [count, output, key, words]
    #     print('{0} ==> {1} ({2}) {3}'.format(count, output, key, words))

    # best_results = sorted(best_results, key=lambda x: x[1], reverse=True)

  print ("sorted:")
  for result in best_results:
    print (result)

if __name__ == "__main__":
   main(sys.argv[1:])