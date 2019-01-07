import argparse
import sys

import woordzoeker
import ceaser

def test_rotation(cipher, r):
  print('Rotating {0} by {1} characters\n'.format(cipher,r))
  output = ''
  for c in cipher:
    output += (ceaser.substitute(c,r))

  print ("Output with r = {0:+3}:\n{1}".format(r, output))

  return woordzoeker.search_words(output)

def main(argv):
  parser = argparse.ArgumentParser(description='Test Caeser in woordzoeker')
  parser.add_argument('cipher')
  parser.add_argument('-r', '--rot', default=0, type=int, help='Number of places to rotate the alphabet (-13 to +13)')
  args=parser.parse_args()
  cipher=args.cipher
  r=args.rot

  if r == 0:
    # Can be explicitly provided on the command line, or is the default value if none provided
    #print('Rotating {0}\n'.format(cipher))

    answers = []

    for r in range (-13, +14):
      woorden, matrix = test_rotation(cipher, r)
      for woord in woorden:
        answers.append([woord, len(woord)])

    answers = sorted(answers, key=lambda x: x[1], reverse=True)

    print ("sorted:")
    for woord in answers:
      print (woord)

  else:
    test_rotation(cipher, r)

if __name__ == "__main__":
   main(sys.argv[1:])