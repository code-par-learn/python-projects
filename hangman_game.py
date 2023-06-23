from ast import Break
import random
def end(word,min_chance):
    q="_ "*len(word)
    guess_letters=""
    while min_chance>=1:
        guess=str(input("Enter a letter:"))

        if guess.isnumeric():
            print("letters only")
            min_chance-=1
            continue
        if len(guess)>1:
            print('one letter only')
            min_chance-=1
            continue
        if guess in guess_letters:
            print("you have already guessed it")
            min_chance-=1
            continue
        #main check
        if guess in word:
            ors=word.count(guess)
            for i in range(ors):
                guess_letters += guess
            for i in word:
                if i in guess_letters and len(guess_letters)!=len(word):
                    print(i,end=' ')
                elif len(guess_letters)==len(word):
                    print("you won")
                    print("the word is")
                    return word
                else:
                    print("_",end=' ')
            print()                         
        else:
            print("try again its not the correct letter")
    else:
        print("sorry all the chances are gone")
        print("The word is ",word)
def start():
    veges=["potato","tomato","brinjal","cabbage","radish","onion","cauliflower","carrot","pumpkin"]
    word=random.choice(veges)
    length=len(word)
    min_chance=length+1
    ques_str="_ "*length
    print("Guess the word  (HINT:its a vegetable) ")
    print(ques_str)
    return end(word,min_chance)  
result=start()        
print(result)    


