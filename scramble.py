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

import time
from functools import partial

def npermutations(l):
    num = factorial(len(l))
    return num

def test_string(cap, keytupple):
  #print(keytupple)

  teststring = cap
  for i in keytupple:
    teststring += i

  words = re.findall(r"[\w']+", teststring)

  indiccount = dict.spell(words[0])

  if indiccount == 0:
    return teststring, 0

  for word in words[1:]:
  # print the word
    if (len(word) > 2):
      testdict = dict.spell(word)
      if (testdict):
        indiccount += 1
      #print(word, testdict)

 #print (teststring, int(100 * indiccount / len(words)))

  return teststring, int(100 * indiccount / len(words))

def main(argv):
  f= open("scramble.txt","a")

  parser = argparse.ArgumentParser(description='test all position combination of the letters and count the number of words which are in a dictionary')
  parser.add_argument('cipher')
  parser.add_argument('-t', '--threshold', default=70, type=int, help='minimim percentage of words to be know')

  args=parser.parse_args()
  puzzle = args.cipher
  threshold = args.threshold

  

  print ("Puzzle: ", puzzle)

  simplified = ''
  caps = ''

  for i in puzzle:
    if i.isalpha():
      if i.isupper():
        caps += i
      else:
        simplified += i


  print("Caps   ", caps)
  print("others ", simplified)
    

  answer = {}
  puzzle_lenght = len(simplified)
  print ("length of puzzle", puzzle_lenght)

  nr_strings = npermutations(simplified) * npermutations(caps)

  print("generating test values.." , nr_strings)

  f.write('Test: {0} ==> {1}\n\n\n'.format(simplified, nr_strings))
  f.flush()

  counter = 0
  progress = 100.0

  starttime = time.time()
  with multiprocessing.Pool() as pool: # default is optimal number of processes
        #results = pool.map(do_stuff, itertools.permutations('1234', r=4))
        for cap in caps:
          print ("Cap", cap)
          capindex = caps.find(cap)
          other_caps = caps[:capindex] + caps[capindex+1:]
          print ("Other Caps", other_caps)

          func = partial(test_string, cap)

          for line, indiccount in pool.imap_unordered(func, itertools.permutations(other_caps + simplified)):
            counter += 1
            new_progress = int(100000 * counter/nr_strings)/1000
            if (new_progress != progress) or (counter % 100000 == 0):
              current_time = time.time()
              difference = int(current_time - starttime)
              remaining_time = (difference * nr_strings / counter) / 3600
              print("Progress: {0}% - {1} values - {2} hours remaining".format(new_progress, counter, remaining_time), end="\r", flush=True)
              progress = new_progress
            if indiccount >= threshold:
              print ("\n", line, indiccount)
              answer[line] = indiccount
              f.write('{0} ==> {1}%\n'.format(line, indiccount))
              f.flush()

        pool.close()
        pool.join()

  print("\n\n...done")
  
  sorted_answer = sorted(answer.items(), key=operator.itemgetter(1), reverse=True)

  for item in sorted_answer:
      print(item)
      f.write('{0}\n'.format(item))

  f.close() 


  

if __name__ == "__main__":
   main(sys.argv[1:])
