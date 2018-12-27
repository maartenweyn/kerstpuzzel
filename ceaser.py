import argparse
import sys

import hunspell

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
  parser = argparse.ArgumentParser(description='Decode a message hidden by a Caesar cipher.')
  parser.add_argument('cipher')
  parser.add_argument('-r', '--rot', default=0, type=int, help='Number of places to rotate the alphabet (-13 to +13)')
  args=parser.parse_args()
  cipher=args.cipher
  r=args.rot

  try:
    r = int(r)  
  except (ValueError, NameError):
    # Code to execute if not a number or not defined
    # parser default value of 0 should prevent this
    print('Rotating {0}\n'.format(cipher))
    for r in range (-13, +14):
      output = ''
      for c in cipher:
        output += (substitute(c,r))
      print('{0:+3} --> {1}'.format(r, output))
  else:
    # Code to execute if it is a number
    if r == 0:
      # Can be explicitly provided on the command line, or is the default value if none provided
      print('Rotating {0}\n'.format(cipher))

      success = {"r":-100}

      for r in range (-13, +14):
        output = ''
        for c in cipher:
          output += (substitute(c,r))

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
        else:
          indic = False

        
        print('{0:+3} ==> {1} {2}'.format(r, output, indic))

        if (indic):
          success["r"] = r
          success["output"] = output

      if (success["r"] > -100):
        print('Found it {0:+3} ==> {1}'.format(success["r"], success["output"]))

    else:
      print('Rotating {0} by {1} characters\n'.format(cipher,r))
      output = ''
      for c in cipher:
        output += (substitute(c,r))
      print('{0:+3} ==> {1}'.format(r, output))

if __name__ == "__main__":
   main(sys.argv[1:])
