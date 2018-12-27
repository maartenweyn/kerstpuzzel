import argparse
import sys

#atbash


def substitute(c):
  if c.isalpha():
    if ord(c) in range(97,123):
      return chr(109 + (110 - ord(c)))
    elif ord(c) in range(65,91):
      return chr(77 + (78 - ord(c)))
    else:
      print("should not happen")
      return(c)
  else:
    #print(c)
    return(c)

def main(argv):
  parser = argparse.ArgumentParser(description='Decode a message hidden by a Caesar cipher.')
  parser.add_argument('cipher')
  parser.add_argument('-r', '--rot', default=0, type=int, help='Number of places to rotate the alphabet (-13 to +13)')
  args=parser.parse_args()
  cipher=args.cipher
  
  output = ''
  ords = ' '
  for c in cipher:
    output += (substitute(c))
  print('--< {0}\n--> {1} '.format(cipher, output))
  

if __name__ == "__main__":
   main(sys.argv[1:])
