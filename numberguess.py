import random as r

random_number = r.randrange(1,100) #Generating Random Number

print(random_number)

score = 110   
chances = 1
while(chances<=10):
  print(f'YOU HAVE {10-chances} CHANCES LEFT')
  guess_number = int(input('Guess the Number : '))

  if(random_number == guess_number):
    print(f'You Won. Score : {score-10*chances} ')
    break
  elif(random_number > guess_number):
    print('Hint : Choose a Higher Number')
  else:
    print('Hint : Choose a Lower Number')
  chances = chances + 1
else:
  print('Oops!! You lost , ran out of your chances.')
