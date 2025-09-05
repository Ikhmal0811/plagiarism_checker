import random

f = open("word.txt", "r")

#def checkWords(theWords):


words = f.read().splitlines()
countWords = len(words)

randomIndex = random.choice(words)

print(randomIndex)

#i = 0
#while(i < countWords):
#    splitwords = words[i].split()
#    checkWords(splitwords)
#    print(words[i])
#    i+=1
