import random

f = open("word.txt", "r")

words = f.read().splitlines()
countWords = len(words)
count = 5#counting the number of try
index = 0
wrongWords = [] 
turn = False

print("Hello this wordle game only have 5 letter, use Uppercase letter for the input")

randomWords = random.choice(words)

def checkAnswer(humanInput, randomWords):
    score = 0;
    for i in range(len(randomWords)):
        if(randomWords[i] == humanInput[i]):
            print(f"{humanInput[i]} correct spot")
            score+=1
        elif humanInput[i] in randomWords:
            print(f"{humanInput[i]} in words but wrong spot")
        else:
            print(f"{humanInput[i]} not in the word")
            if humanInput[i] not in wrongWords:
                wrongWords.append(humanInput[i])
    return score

print(randomWords)

while(count > 0):
    print(f"you have {count} try left\n")
    humanInput = input("insert you input hear: ")
    if len(humanInput) != 5 or not humanInput.isupper(): 
        print("Please input 5 letter only an no lowercase\n")
    else:
        if checkAnswer(humanInput, randomWords) == 5:
            print(f"congrats, you got it right: {randomWords}")
            turn = True
            break
        print(f"here is your wrong letter : {wrongWords}")   
        count-=1


if turn == False :
    print(f"Sorry, you lose. The words was {randomWords}")
