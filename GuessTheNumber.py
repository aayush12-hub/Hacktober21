import sys
import random

def start():
    
    st = input("Press 'S' to start  \n      'X' to end ->")
    if(st=='s' or st == 'S'):
        randNum()
    elif(st=='x' or st=='X'):
        sys.exit("Thanks for palying")
    else:
        print("Invalid Choice !!! Please try again...")
        start()

def randNum():
    global secretNum 
    secretNum = random.randint(1,100)
    print(secretNum)
    guess()

def guess():
    global guessNum
    guessNum = int(input("Guess any number between 1 - 100 -> "))
    result()

def result():
    if(guessNum == secretNum):
        print("Whoaa!!..Lucky You > <")
        #start()
    else:
        print("Try again !!" )
    start()

print("-- Lucky Guess --")
start()