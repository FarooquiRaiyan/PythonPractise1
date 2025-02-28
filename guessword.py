import random

words=["hello","choice","good","bad","worst","think","dsa","raiyan"]

rndm_guess=random.choice(words)
print(rndm_guess)

input_word=input("enter the word for guess")

while (input_word!= 'Exit'):
    if input_word in  rndm_guess:
        print("you guess it write")
    else:
        print("sorry wrong")