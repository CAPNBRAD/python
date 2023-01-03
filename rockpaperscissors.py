def start():
    print('This is my Rock Paper Scisors Game!')
    Player_one = 'Brad'
    Player_two = 'Maddox'

    def choices(Player_one_choice, Player_two_choice):
        if Player_one_choice == 'rock' and Player_two_choice == 'paper':
            return('Paper covers Rock!' + Player_two + ' wins!')
        elif Player_one_choice == 'paper' and Player_two_choice == 'rock':
            return('Paper covers Rock! ' + Player_one + ' wins!')
        elif Player_one_choice == 'scissors' and Player_two_choice == 'paper':
            return('Scissors cuts Paper! ' + Player_one + ' wins!')
        elif Player_one_choice == 'rock' and Player_two_choice == 'scissors':
            return('Rock smashes Scissors! ' + Player_one + ' wins!')
        elif Player_one_choice == 'paper' and Player_two_choice == 'scissors':
            return('Scissors cuts Paper! ' + Player_two + ' wins!')
        elif Player_one_choice == Player_two_choice:
            return('Brad and Maddox tied!')
        else:
            return('Please type Rock, Paper or Scissors!')
    Player_one_choose = input('Does ' + Player_one +
                                     ' choose Rock, Paper or Scissors? ').lower()
    Player_two_choose = input('Does ' + Player_two +
                                     ' choose Rock, Paper or Scissors? ').lower()
    print(choices(Player_one_choose, Player_two_choose))

    def Play_Again():
        Again = input('Would you lke to play the game again? ').lower()
        if Again== 'No'.lower():
                    quit()
        if Again== 'Yes'.lower():
                    start()
        else:
            print('Please enter Yes or No. Thank you!')
            Play_Again()
    Play_Again()
start()
