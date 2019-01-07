import argparse
import sys

import hunspell
import itertools
import multiprocessing

from multiprocessing import Pool

dict = hunspell.HunSpell('Spelling/nl_NL.dic', 'Spelling/nl_NL.aff')
f= open("vigenere.txt","a")

success = []
cipher = ''

print("Number of cpu : ", multiprocessing.cpu_count())

## based on https://github.com/dnlongen/CaesarsHelper/blob/master/caesar.py

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def substitute(c,r):
  "Rotate the character by rot characters; wrap if >Z or <A"
  if c.isalpha():
    if ord(c) in range(97,123):
      if ord(c)+r in range(97,123):
        #print(c, " --> ", ord(c), " --> ", ord(c)+r, " --> ", chr(ord(c)+r))
        return chr(ord(c)+r)
      elif ord(c)+r > 122:
        #print(c, " --> ", ord(c), " --> ", ord(c)+r-26, " --> ", chr(ord(c)+r))
        return chr(ord(c)+r-26)
      elif ord(c)+r < 97:
        return chr(ord(c)+r+26)
      else:
        print ('this should not happen')
    elif ord(c) in range(65,91):
      if ord(c)+r in range(65,91):
        #print(c, " --> ", ord(c), " --> ", ord(c)+r, " --> ", chr(ord(c)+r))
        return chr(ord(c)+r)
      elif ord(c)+r > 90:
        #print(c, " --> ", ord(c), " --> ", ord(c)+r, " --> ", chr(ord(c)+r))
        return chr(ord(c)+r-26)
      elif ord(c)+r < 65:
        return chr(ord(c)+r+26)
      else:
        print ('this should not happen')
    else:
      print ('this should not happen')
  else:
    #print(c)
    return(c)

def search_tupple(cipher, key, max_length):
  global f
  index = 0
  output1 = ''
  output2 = ''
  keylength = len(key)
  for c in cipher:
    r = key[index % keylength]
    if ord(c.lower()) in range(97,123):
      output1 += (substitute(c,ord(r.lower())-97))
      index += 1
    else:
      output1 += c
  
  for c in cipher:
    r = key[index % keylength]
    if ord(c.lower()) in range(97,123):
      output2 += (substitute(c,ord(r.lower())-97))
    
    index += 1

  word1 = output1[:keylength]
  word2 = output2[:keylength]
  testdict1 = dict.spell(word1)
  testdict2 = dict.spell(word2)
  
  if (testdict1 or testdict2):
    if keylength < max_length:
      for l in LETTERS:
        new_key = key + l
        search_tupple(cipher, new_key, max_length)
    else:
      if (testdict1):
        f.write('{0} ==> {1}\n'.format(key, output1))
        print('{0} ==> {1}'.format(key, output1))
        success.append({"key":key, "output":output1})
      if (testdict2):
        f.write('{0} ==> {1}\n'.format(key, output2))
        print('{0} ==> {1}'.format(key, output2))
        success.append({"key":key, "output":output2})
    f.flush()
  
def test_key(data):
    global verbose

    key = data[0]
    cipher = data[1]
    verbose = data[2]
    #  keytupple = (10, 0)
    #print (keytupple)
    #print (key)

    #f.write('{0}\n'.format(key))
    #f.flush()

    index = 0
    output = ''
    #print ("cipher", cipher)
    for c in cipher:
      r = key[index % len(key)]
      if ord(c.lower()) in range(97,123):
        #output += (substitute(c,r))
        output += (substitute(c,ord(r.lower())-97))
      index += 1
      
    indiccount = 0

    start = 0
    antwoord = {}
    while len(output[start:]) > 3:
      wordFound = False
      #print (words, len(words))
      for i in range(len(output[start:]), 3, -1):
        #print("testing {0} at {1} to {2}".format(words[:i], start, i))
        #if (len(words[:i]) > 3):
          if (dict.spell(output[start:start+i])):
            #if words[:i] not in antwoord:
            antwoord[output[start:start+i]] = [start, i, len(output[start:start+i])]
            indiccount += 1
            start += i
            wordFound = True
            break
      if (not wordFound):
        start += 1


    #print (antwoord)

    if (indiccount > 5):
      indic = True
      f.write('{3}: {0} ==> {1} {2} \n'.format(key, output, indic, indiccount))
      f.flush()
    else:
      indic = False

    if verbose:  
      print('{3}: {0} ==> {1} {2} '.format(key, output, indic, indiccount))

    if (indic):
      success.append({"key":key, "output":output})

def main(argv):
  global f
  global success

  p = Pool(multiprocessing.cpu_count())

  parser = argparse.ArgumentParser(description='Decode a message hidden by a vigenere cipher.')
  parser.add_argument('cipher')
  parser.add_argument('-l', '--keylength', default=0, type=int, help='Length of key')
  parser.add_argument('-k', '--key', default='', help='key')
  parser.add_argument('-t', '--test', default=0, help='only test key length for dict')
  parser.add_argument('-s', '--start', default=0, type=int, help='Length of key')
  parser.add_argument('-p', '--stop', default=0, type=int, help='Length of key')
  parser.add_argument('-v', '--vebose', default=0, type=int, help='Verbose')

  args=parser.parse_args()
  cipher=args.cipher.lower()
  key = args.key
  keylength = args.keylength
  verbose = args.vebose

  
  print('Cipher {0}\n'.format(cipher))

  if key != '':
    # Can be explicitly provided on the command line, or is the default value if none provided

    keylength = len(key)
    print ("key:", key, keylength)

    index = 0
    output1 = ''
    output2 = ''
    for c in cipher:
      r = key[index % keylength]
      if ord(c.lower()) in range(97,123):
        output1 += (substitute(c,ord(r.lower())-97))
        index += 1
        #print (index, index % keylength, c, output)
      else:
        output1 += c

    index = 0
    for c in cipher:
      r = key[index % keylength]
      if ord(c.lower()) in range(97,123):
        output2 += (substitute(c,ord(r.lower())-97))
        #print (index, index % keylength, c, output)
      else:
        output2 += c
      index += 1

    if verbose:
      print('{0} ==> {1}'.format(key, output1))
      print('{0} ==> {1}'.format(key, output2))
  else:

    if keylength == 0:
      #dept search
      
      f.write('{0}\n'.format(cipher))
      f.write('keylength {0}\n'.format(keylength))
      f.flush()
      
      # Can be explicitly provided on the command line, or is the default value if none provided
      print('Rotating {0}\n'.format(cipher))

      keylength = args.start

      #if True:
      for keytupple in itertools.product(range(26), repeat=keylength):
      #  keytupple = (10, 0)
        #print (keytupple)

        search_tupple(cipher, key, args.stop)

        index = 0
        output = ''
        for c in cipher:
          r = keytupple[index % keylength]
          if ord(c.lower()) in range(97,123):
            output += (substitute(c,r))
            index += 1
            #print (index, index % keylength, c, output)
          else:
            output += c

        if args.test:
          words = output[:keylength]
        else:
          words = output.split()
          
        indiccount = 0
        for word in words:
        # print the word
          testdict = dict.spell(word)
          if (testdict):
            indiccount += 1
          #print(word, testdict)

        if (indiccount > len(words) * 0.6):
          indic = True
          f.write('{0} ==> {1} {2}\n'.format(key, output, indic))
          f.flush()
        else:
          indic = False

        if verbose:  
          print('{0} ==> {1} {2}'.format(key, output, indic))

        if (indic):
          success.append({"key":key, "output":output})
    else:
      f= open("vigenere.txt","a")
      f.write('{0}\n'.format(cipher))
      f.write('keylength {0}\n'.format(keylength))
      f.flush()
      
      success = []
      
      for keytupple_prefix in itertools.product(range(26), repeat=2):
        keys = []
        key_prefix = ''
        for i in keytupple_prefix:
          key_prefix += LETTERS[i]

        for keytupple in itertools.product(range(26), repeat=keylength-2):
          key = key_prefix
          for i in keytupple:
            key += LETTERS[i]
          keys.append([key, cipher, verbose])
          
        print("starting with ", key_prefix, len(keys) )
        p.map(test_key, keys)
        print("ending ", key_prefix)

      

    if (len(success) > 0):
      for item in success:
        print('Found it {0} ==> {1}'.format(item["key"], item["output"]))
    else:
      print("Nothing found")
      f.write("Nothing Found\n\n\n")

      f.close()  

if __name__ == "__main__":
   main(sys.argv[1:])
