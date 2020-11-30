'''
Rock paper scissors game using conditionals and random class
'''

import random

choice = int(input("What do you choose?: 0 for Rock, 1 for paper, 2 for scissors: "))
computer_choice = random.randint(0,2)



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
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
map = [rock, paper, scissors]
if choice ==computer_choice:
  print(f"{map[choice]}\n computer choice \n{map[computer_choice]} \n draw")
elif choice==0 and computer_choice>0:
  if computer_choice ==2:
    print(f"{map[choice]}\n computer choice \n{map[computer_choice]} \n you win")
  else:
    print(f"{map[choice]}\n computer choice \n{map[computer_choice]} \n you loose")
elif choice ==1 and computer_choice>1:
  if computer_choice ==2:
    print(f"{map[choice]}\n computer choice \n{map[computer_choice]} \n you loose")
  else:
     print(f"{map[choice]}\n computer choice \n{map[computer_choice]} \n you win")
elif choice ==1 and computer_choice==0:
  print(f"{map[choice]}\n computer choice \n{map[computer_choice]} \n you win")
else:
  print(f"{map[choice]}\n computer choice \n{map[computer_choice]} \n you loose")

