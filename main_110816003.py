import random

stone = '''
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

game_images = [stone, paper, scissors]

print("請選擇要出什麼?")
user = int(input("石頭請輸入0, 布請輸入1, 剪刀請輸入2 "))
print(game_images[user])

print("電腦出")
computer = random.randint(0, 2)
print(game_images[computer])

if user == 0:
    if computer == 0:
        print("平手")
    elif computer == 1:
        print("你輸了")
    else:
        print("你贏了")

if user == 1:
    if computer == 1:
        print("平手")
    elif computer == 2:
        print("你輸了")
    else:
        print("你贏了")

if user == 2:
    if computer == 2:
        print("平手")
    elif computer == 0:
        print("你輸了")
    else:
        print("你贏了")
