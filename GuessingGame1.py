import random

def high_or_low(num1, num2):
    if num1 > num2:
        return "It's lower than "+str(num1)
    if num1 < num2:
        return "It's higher than "+str(num1)
    if num1 == num2:
        return 0

def game():

    correct = 0
    num2 = random.randint(1, 9)
    print("   The Game Has Started!!")
    print("_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_")
    ct = 1
    while correct == 0:
        print("Round " + str(ct))
        num1 = int(input(("Pick a number between 1 and 9: ")))
        if high_or_low(num1, num2) == 0:
            print("It's exactly "+str(num1)+" !")
            print('You have won after just '+str(ct)+' Rounds, congratulations!')
            correct = 1
        else: print(high_or_low(num1, num2))

        ct += 1




game()