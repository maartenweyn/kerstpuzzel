import argparse
import sys
import operator

freq = {

}


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
  parser = argparse.ArgumentParser(description='Show frequency of letters')
  parser.add_argument('cipher')
  args=parser.parse_args()
  cipher=args.cipher

  for o in range(65,91):
    freq[chr(o)] = 0
  
  freq["other"] = 0

  for c in cipher:
    if c.isalpha():
      if ord(c) in range(97,123):
        freq[c.capitalize()] += 1
      elif ord(c) in range(65,91):
        freq[c] += 1
    else:
      freq["other"] += 1

  sorted_x = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)

  print(freq)
  print(sorted_x)
  

if __name__ == "__main__":
   main(sys.argv[1:])
