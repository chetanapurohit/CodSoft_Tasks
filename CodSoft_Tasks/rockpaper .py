import random
print("~~~~~~~~~~~~~~~rock paper scissor~~~~~~~~~~~~~")

rock = '''
     _______
---'    ____)
       (_____)
       (_____)
       (____)
---,__(___)
'''

paper = '''
     ________
---'    _____)_____
           ________)
           __________)
           _________)
---. ____________)
'''

scissor = '''
     ________
---'    _____)_____
           ________)
           __________)
        (_____)
---.__(____)
'''

game_images = [rock, paper, scissor]
user_choice = int(input("enter your choice : type 0 for rock, 1 for paper, 2 for scissor \n"))
if user_choice >= 3 or user_choice < 0:
    print("you entered invalid number, you lose")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print("computer chose:", game_images[computer_choice])
    if computer_choice == user_choice:
         print("it is a drow") 
    elif computer_choice == 0 and user_choice == 2:
         print("you lose") 
    elif user_choice == 0 and computer_choice == 2:
        print("you win")
    elif computer_choice > user_choice:  #2>0
        print("you lose")
    elif user_choice > computer_choice:  #2>0
        print("you win")
    
  
