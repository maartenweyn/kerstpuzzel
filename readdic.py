f = open("Spelling/nl_NL.dic", "r") 

for line in f:
  word =  line.strip().split('/')[0]
  if len(word) == 16:
    print (word)

