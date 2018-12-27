import argparse
import sys

import hunspell
import itertools

dict = hunspell.HunSpell('/Library/Spelling/nl_NL.dic', '/Library/Spelling/nl_NL.aff')


## based on https://github.com/dnlongen/CaesarsHelper/blob/master/caesar.py


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

def main(argv):
  parser = argparse.ArgumentParser(description='Decode a message hidden by a vigenere cipher.')
  parser.add_argument('cipher')
  parser.add_argument('-k', '--keylength', default=0, type=int, help='Length of key')

  args=parser.parse_args()
  cipher=args.cipher

  keylength = args.keylength


  f= open("vigenere.txt","a")
  f.write('{0}\n'.format(cipher))
  f.write('keylength {0}\n'.format(keylength))
  f.flush()
  
  # Can be explicitly provided on the command line, or is the default value if none provided
  print('Rotating {0}\n'.format(cipher))

  success = []

  #if True:
  for keytupple in itertools.product(range(26), repeat=keylength):
  #  keytupple = (10, 0)
    #print (keytupple)

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
      f.write('{0} ==> {1} {2}'.format(keytupple, output, indic))
      f.flush()
    else:
      indic = False

      
      print('{0} ==> {1} {2}'.format(keytupple, output, indic))

    if (indic):
      success.append({"key":keytupple, "output":output})

  if (len(success) > 0):
    for item in success:
      print('Found it {0} ==> {1}'.format(item["key"], item["output"]))
  else:
    print("Nothing found")
    f.write("Nothing Found")

  f.close()

if __name__ == "__main__":
   main(sys.argv[1:])