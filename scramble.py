import argparse
import sys

import hunspell
import itertools
import multiprocessing
from multiprocessing import Pool
import re

import operator
from collections import Counter
from math import factorial
dict = hunspell.HunSpell('Spelling/nl_NL.dic', 'Spelling/nl_NL.aff')

def npermutations(l):
    num = factorial(len(l))
    return num

def test_string(keytupple):
  #print(keytupple)

  teststring = ''
  for i in keytupple:
    teststring += i

  words = re.findall(r"[\w']+", teststring)

  indiccount = 0
  for word in words:
  # print the word
    if (len(word) > 1):
      testdict = dict.spell(word)
      if (testdict):
        indiccount += 1
      #print(word, testdict)

  #print (words, " ->", indiccount)

  return teststring, indiccount

def main(argv):
  #p = Pool(multiprocessing.cpu_count())

  parser = argparse.ArgumentParser(description='test all position combination of the letters and count the number of words which are in a dictionary')
  parser.add_argument('cipher')
  parser.add_argument('-t', '--threshold', default=1, type=int, help='minimim number of words')

  args=parser.parse_args()
  puzzle = args.cipher
  threshold = args.threshold

  puzzle_lenght = len(puzzle)

  answer = {}

  print ("length of puzzle", puzzle_lenght)

  nr_strings = npermutations(puzzle)

  print("generating test values.." , nr_strings)

  counter = 0

  with multiprocessing.Pool() as pool: # default is optimal number of processes
        #results = pool.map(do_stuff, itertools.permutations('1234', r=4))
        for line, indiccount in pool.imap_unordered(test_string, itertools.permutations(puzzle)):
          counter += 1
          print("Progress: {}%".format(int(100 * counter/nr_strings)), end="\r", flush=True)
          if indiccount >= threshold:
            print ("\n", line, indiccount)
            answer[line] = indiccount

  print("...done")
  
  sorted_answer = sorted(answer.items(), key=operator.itemgetter(1), reverse=True)

  for item in sorted_answer:
      print(item)


  

if __name__ == "__main__":
   main(sys.argv[1:])
