import random

while True:
    print('Hello, welcome to rock, paper, sciessors. Please choose from the menu below: ')
    print('1 : Rock')
    print('2 : Paper')
    print('3 : Scissors')
    print('4 : QUIT GAME')
    choice = input('Enter choice')
    opp_choice = random.randint(1, 3)
    
    if choice.lower().strip() in ['1', 'rock']:
        if opp_choice == 1:
            print("you chose rock, your opponent chose rock. It's a TIE.")
        if opp_choice == 2:
            print("you chose rock, your opponent chose paper. You LOSE.")
        if opp_choice == 3:
            print("you chose rock, your opponent chose scissors. You WIN.")
    elif choice.lower().strip() in ['2', 'paper']: 
        if opp_choice == 1:
            print("you chose paper, your opponent chose rock. You WIN.")
        if opp_choice == 2:
            print("you chose paper, your opponent chose paper. It's a TIE.")
        if opp_choice == 3:
            print("you chose paper, your opponent chose scissors. You LOSE.")
    elif choice.lower().strip() in ['3', 'scissors']:
        if opp_choice == 1:
            print("you chose scisssors, your opponent chose rock. You LOSE")
        if opp_choice == 2:
            print("you chose scisssors, your opponent chose paper. You WIN.")
        if opp_choice == 3:
            print("you chose scisssors, your opponent chose scissors. It's a TIE.")

    elif choice.lower().strip() in ['4', 'quit', 'quit game', 'quitgame']:
        print('So you have chosend death')
        break 
