import random

f = open("word.txt", "r")

words = f.read().splitlines()
countWords = len(words)
count = 5#counting the number of try
index = 0

print("Hello this wordle game only have 5 letter, use Uppercase letter for the input")

randomWords = random.choice(words)

def checkAnswer(humanInput, randomWords):
    for i in range(len(randomWords)):
        if(randomWords[i] == humanInput[i]):
            print(f"{humanInput[i]} correct spot")
        elif humanInput[i] in randomWords:
            print(f"{humanInput[i]} in words but wrong spot")
        else:
            print(f"{humanInput[i]} not in the word")

print(randomWords)

while(count > 0):
    print(f"you have {count} try left")
    humanInput = input("insert you input hear: ")
    checkAnswer(humanInput, randomWords)

    count-=1



