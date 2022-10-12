rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)
          ______)
       __________)
      (____)
---.__(___)
'''

import random
play_game = input("Want to play Rock, Paper, Scissors? Type Yes or No: ")
is_play_game = True
while play_game == "Yes":

  my_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
  my_number = int(my_choice)
  if my_number >=3 or my_number<0:
    print("Invalid number. Try again!")
  else:
    comp_number = random.randint(0,2)
    # my selection
    rps = [rock, paper, scissors]
    my_selection = rps[my_number]
    # comp selection
    comp_choice = rps[comp_number]
    print(f"Your choice is:{my_selection}")
    print(f"Computer choice is: {comp_choice}")
    if my_number == comp_number:
      print("The score is draw")
    elif my_number == 0 and comp_number == 1 or my_number == 1 and comp_number == 2 \
            or my_number == 2 and comp_number == 0:
      print("You lose!")
    elif my_number == 0 and comp_number == 2 or my_number == 2 and comp_number == 1 \
            or my_number == 1 and comp_number == 0:
      print("You won!")
  if is_play_game == False:
    print("Game over")