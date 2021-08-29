import random
import time
print("welcome to the funzone here we play rock paper scissors game")
print("2 types of game mode is avialable")
print("1.playing with the  computer  \n 2.plying with another player")
print(" choose the game mode ")
mode=int(input());
list = ["rock", "paper", "scissor"]
total_amount=5000
history={}
if(mode==1):
    for i in range (1,6):
        print(f"you have {total_amount} rs now")
        flag=0
        print("user turn ")
        print(f"chose value from{list}")
        user_action=input()
        print("now it's computer turn")
        computer_action=random.choice(list)
        print(f"computer chose {computer_action}")
        time.sleep(1.0)
        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
            history[i]=f"both player selected {user_action} so match is tie"
        elif user_action == list[0]:
            if computer_action == list[2]:
                flag=1
                print("Rock smashes scissors! You win!")
                total_amount+=2000
            else:
                print("Paper covers rock! You lose.")
                total_amount -= 1000
            if(flag==1):
                history[i]=f"you select {user_action} and computer chose {computer_action} so you win 2000 rs"
            else:
                history[i]=f"you select {user_action} and computer chose {computer_action} so you lose  1000 rs"
        elif user_action == list[1]:
            if computer_action == list[0]:
                print("Paper covers rock! You win!")
                flag=1
                total_amount += 2000
            else:
                print("Scissors cuts paper! You lose.")
                total_amount -= 1000
            if (flag == 1):
                history[i] = f"you select {user_action} and computer chose {computer_action} so you win 2000 rs"
            else:
                history[i] = f"you select {user_action} and computer chose {computer_action} so you lose  1000 rs"
        elif user_action == list[2]:
            if computer_action == list[1]:
                print("Scissors cuts paper! You win!")
                flag=1
                total_amount += 2000
            else:
                print("Rock smashes scissors! You lose.")
                total_amount -= 1000
            if (flag == 1):
                history[i] = f"you select {user_action} and computer chose {computer_action} so you win 2000 rs"
            else:
                history[i] = f"you select {user_action} and computer chose {computer_action} so you lose  1000 rs"
    time.sleep(2.0)
    print("now lets'check history of the game")
    for i in range(1,6):
        print(f"in {i} game {history[i]}")
    earning_vlue=total_amount-5000
    if(earning_vlue==0):
        print("in this game nither you earn nor you lose")
    elif(earning_vlue>0):
        print(f"in this game you earn {earning_vlue}")
    else:
        earning_vlue=-earning_vlue
        print(f"in this game you lose {earning_vlue} money")
else:
    history={}
    amount_1=5000
    amount_2=5000
    for i in range(1,6):
        flag1 = 0
        flag2 = 0
        print("user 1 turn")
        print(f"chose any one from {list}")
        val1=int(input())
        random.shuffle(list)
        final_val1=list[val1]
        print(f"user 1 chose {val1} no thing")
        print("user 2 turn")
        print(f"chose any one from {list}")
        val2 = int(input())
        print(f"user 2 chose {val2} no thing")
        random.shuffle(list)
        final_val2=list[val2]
        print(f"player 1 chose {final_val1} and player 2 select {final_val2}")
        if(final_val1==final_val2):
            print(f"both player select the {final_val2} so match is trie")
        elif final_val1=="paper":
            if(final_val2=="rock"):
                flag1=1
                amount_1+=2000
                amount_2-=1000
                print("Paper covers rock! player 1 win.")
            else:
                flag2=1
                amount_2 += 2000
                amount_1 -= 1000
                print("Scissors cuts paper! player 2  win!")
        elif final_val1=="rock":
            if(final_val2=="scissor"):
                flag1=1
                amount_1 += 2000
                amount_2 -= 1000
                print("Rock smashes scissors! player 1 win.")
            else:
                flag2=1
                amount_2 += 2000
                amount_1 -= 1000
                print("Paper covers rock! player 2 win.")
        elif final_val1=="scissor":
            if(final_val2=="paper"):
                flag1=1
                amount_1 += 2000
                amount_2 -= 1000
                print("Scissors cuts paper! player 1  win!")
            else:
                flag2=1
                amount_2 += 2000
                amount_1 -= 1000
                print("Rock smashes scissors! player 2 win.")
        if(flag1==1):
            history[i]=f"player 1 earn 2000 rs while player 2 lose 1000 rs and player 1 have {amount_1} rs while player 2 have {amount_2}rs"
        elif(flag2==1):
            history[
                i] = f"player 2 earn 2000 rs while player 1 lose 1000 rs and player 1 have {amount_1} rs while player 2 have {amount_2}rs"
        else:
            history[i]=f"both player select same thing so match is tie and player 1 have {amount_1} rs while player 2 have {amount_2}rs"
    time.sleep(2.0)
    print("now check the history of the game")
    for i in range (1,6):
        print(f"in game  {i} {history[i]}")
    diff1=amount_1-5000
    diff2=amount_2-5000
    if(diff1==0):
        print("player 1 nither earn nor lose money")
    elif diff1>0:
        print(f"player 1 earn {diff1} rs")
    else:
        diff1=-diff1
        print(f"player 1 lose {diff1} rs")
    if (diff2 == 0):
        print("player 2 nither earn nor lose money")
    elif diff2 > 0:
        print(f"player 2 earn {diff2} rs")
    else:
        diff2 = -diff2
        print(f"player 2 lose {diff2} rs")















