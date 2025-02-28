import random

words=["hello","choice","good","bad","worst","think","dsa","raiyan"]

rndm_guess=random.choice(words)
print(rndm_guess)


guess_count=0
input_word=""

while input_word!= 'Exit':
    input_word=input("enter the word for guess")
    if input_word in  rndm_guess:
        print("you guess it write")
        exit()
    elif input_word =='Exit':
        print("Exiting")
    elif input_word not in rndm_guess:
        guess_count=guess_count+1
        print("sorry try again your count is this ",guess_count)
        if guess_count>12:
            print("your guess count is 12  so exiting the program",guess_count)
            exit()
   