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

chop_length = 10

def npermutations(l):
    num = factorial(len(l))
    return num

def test_string(cap, full_test_string, sentence, keytupple):
  

  teststring = cap
  for i in keytupple:
    teststring += i

  #print("teststring", teststring)

  words = re.findall(r"[\w']+", teststring)
  restofstring = full_test_string
  nextword = teststring

  if (len(words) > 0):
    nextword = words[0]

  indiccount = dict.spell(nextword)
  if indiccount == 0:
    #print ("returning fail: {0}, {1}, {2}".format(sentence, sentence.count(' '), len(full_test_string)))
    return sentence, sentence.count(' '), len(full_test_string)

  #print("nextword", nextword)

  for i in nextword:
    letterindex = restofstring.find(i)
    if letterindex >= 0:
      restofstring = restofstring[:letterindex] + restofstring[letterindex+1:]
      #print(i, letterindex, restofstring)

  remainingstringlength = len(restofstring)

  #print("restofstring", restofstring)

  if remainingstringlength < 2:
    sentence = sentence + " " + nextword
    #print ("returning success: {0}, {1}, {2}".format(sentence, sentence.count(' '), remainingstringlength))
    return sentence, len(re.findall(r"[\w']+", sentence)), remainingstringlength


  best = remainingstringlength
  best_count = 100
  best_result = ''

  #counter = 0
  for tupple in itertools.permutations(restofstring, min(chop_length, remainingstringlength)):
    #counter += 1
    #print ("{4} {0} + '{1}', '{2}', ({3})".format('', restofstring, sentence + " " + nextword, tupple, counter))
    result, count, rest = test_string("", restofstring, sentence + " " + nextword, tupple)

    if best_count < count:
      best_count = count
      best_result = result
      best = rest

    #if rest < 2:
      #return result, count, rest

  return best_result, best_count, best



#   for word in words[1:]:
#   # print the word
#     if (len(word) > 1):
#       testdict = dict.spell(word)
#       if (testdict):
#         indiccount += 1
#       #print(word, testdict)

#  #print (teststring, int(100 * indiccount / len(words)))

#   return teststring, int(100 * indiccount / len(words))

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
    if i.isalpha() or i == ' ' or i == ',' or i == '.':
      if i.isupper():
        caps += i
      else:
        simplified += i


  print("Caps   ", caps)
  print("others '{}'".format(simplified))
    

  answer = {}
  puzzle_lenght = len(simplified)
  print ("length of puzzle", puzzle_lenght)

  nr_strings = npermutations(simplified) * npermutations(caps) / factorial(puzzle_lenght-min(chop_length, puzzle_lenght))

  print("generating test values.." , nr_strings)

  f.write('Test: {0} ==> {1}\n\n\n'.format(simplified, nr_strings))
  f.flush()

  counter = 0
  progress = 100.0

  best = puzzle_lenght

  starttime = time.time()
  #with multiprocessing.Pool(1) as pool: # default is optimal number of processes
        #results = pool.map(do_stuff, itertools.permutations('1234', r=4))
  if len(caps) == 0:
    caps = ' '
  for cap in caps:
    print ("Cap", cap)
    capindex = caps.find(cap)
    other_caps = caps[:capindex] + caps[capindex+1:]
    print ("Other Caps", other_caps)

    print ("remaining", other_caps + simplified)

    func = partial(test_string, cap, other_caps + simplified, "")

    #for line, wordcount, remaining in pool.imap_unordered(func, itertools.permutations(other_caps + simplified, min(chop_length, puzzle_lenght))):
    for tupple in itertools.permutations(other_caps + simplified, min(chop_length, puzzle_lenght)):
      line, wordcount, remaining = test_string(cap, other_caps + simplified, "", tupple)
      counter += 1
      new_progress = int(100000 * counter/nr_strings)/1000
      if (new_progress != progress) or (counter % 100000 == 0):
        current_time = time.time()
        difference = int(current_time - starttime)
        remaining_time = (difference * nr_strings / counter) / 3600
        print("Progress: {0}% - {1} values - {2} hours remaining".format(new_progress, counter, remaining_time), end="\r", flush=True)
        progress = new_progress
      if remaining < best:
        #print ("\n", line, wordcount, remaining)
        answer[line] = wordcount
        f.write('{0} ==> {1}%\n'.format(line, wordcount))
        f.flush()
      if remaining <= 1:
          return

        #pool.close()
        #pool.join()

  print("\n\n...done")
  
  sorted_answer = sorted(answer.items(), key=operator.itemgetter(1), reverse=True)

  for item in sorted_answer:
      print(item)
      f.write('{0}\n'.format(item))

  f.close() 


  

if __name__ == "__main__":
   main(sys.argv[1:])
