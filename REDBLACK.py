
import random
list=["red", "black"]

list2=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
list4=["Hearts", "Diamonds", "Spades", "Clubs"]
answer1="lower"
answer2="higher"
answer3="inside"
answer4="outside"
choice=random.choice
#defines variables
Name=input('Please enter your name: ')
print('Hello ' + Name + '!')
print("this is Brads version of the red/black drinking game")
#explains the game
def start():
    choice=random.choice(list)
    guess=input('Please select Red or Black! ')
    print(guess)#guess color of card
    
    if guess!=(choice):
        print("Try again, Take a drink")
        start()#resets on wrong choice
    else: print(" Congrats!!")#victory condition part 1
    choice2=random.choice(range(1,13))
    print(choice2)
    guess2=input("Please select higher or lower, ")
    if guess2==(answer1):
        choice3=random.choice(range(1,13))
        print(random.choice(range(1,13)))
        if choice2<choice3:
            print("try again")
            start()#restarts game on wrong answer
        elif guess2==(answer2):#victory condition 2
            guess2>choice3
            print("try Again")
            start()
        else:#victory part 2

            choice4=random.choice(range(1,13))#still working on this section
            #need to figure out higher or lower than set
            guess3=input("Please select Inside or Outside, ")
            if guess3!= choice2 or choice3:
                print("brad")
            
            #still need suit choices
            
        start()
start()
       
        
        
    
    




















