import random

def importWords():
    wordlist = []
    wordfile = open("words.csv","r")
    for row in wordfile:
        wordlist.append(row)
    wordfile.close()
    for i, s in enumerate(wordlist):
        wordlist[i] = s.rstrip(s[-1])
    return(wordlist)

def addWord():
    wordfile = open("words.csv","a")
    data = input("Enter word: ")
    if data.lower() in wordlist:
        print("Word already in list")
    else:
        wordfile.write(data.lower()+"\n")
    wordfile.close()

def playHangman():
    wordlist = importWords()
    answer = random.choice(wordlist)
    lives = 6
    won = False
    print(f"You have {lives} lives remaining...")
    usertext = ""
    for i in range(len(answer)):
        usertext = usertext+"_ "
    print(usertext)
    while not won:
        if lives <= 0:
            print("You lose")
            break
        guess = input("Enter guess: ")
        if guess == "cheat":
            print(answer)
        if len(guess) != 1:
            print("You must guess a single letter!\n")
        else:
            userinput = ""
            for i in answer:
                if guess == i:
                    userinput += (i)
                else:
                    userinput += ("_")
                    lives -= 1
                    print(f"You have {lives} lives remaining...")
            print(userinput)
playHangman()
#wordlist = importWords()
#print(wordlist)
#addWord()
#wordlist = importWords()
#print(wordlist)
#answer = random.choice(wordlist)
