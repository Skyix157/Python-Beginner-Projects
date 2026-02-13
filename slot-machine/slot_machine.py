import random
import time
from datetime import datetime

print("Hello! Welcome to the Slot Machine Game!")
name = input("What is your name? ")

print("Game Rules: ")
print("If you get three of the same symbol, you win!")
time.sleep(2)

symbols = ["🍒", "🍋", "🍊", "🍇", "🔔"]

while True: 
    tries = 0
    credit = 0
    cost_per_play = 0
    win = False
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    while True:
        try:
            cost_per_play = int(input("Each play price (credit): "))

            if cost_per_play <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except:
            print("Please enter a valid number.")
    print("Good Luck!")

    time.sleep(2)

    while True:
        try:
            credit = int(input("Enter the number of credits you want to play with: "))

            if credit == 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except:
            print("Please enter a valid number.")


    while win == False:
        output = random.choices(symbols, k = 3)
        print("You currently have " + str(credit) + " credits.")

        if credit < cost_per_play:
            if credit == 0:
                print("Sorry, you have no more credits left.")
            else:
                print("Sorry, you only have " + str(credit) + " credits left.")
            time.sleep(1)

            while True:
                answer = input("Buy more credits? ")

                if answer.lower() == "yes":
                        time.sleep(1)

                        while True:
                            try:
                                more_credits = int(input("How many more credits do you want to buy? "))

                                if more_credits <= 0:
                                    print("Please enter a number greater than 0.")
                                    continue
                            except:
                                print("Please enter a valid number.")
                                continue
                            credit += more_credits  
                            break
                        break
                elif answer.lower() == "no":
                    break
                else:
                    print("Please enter yes or no.")
                    continue
            if answer.lower() == "no":
                break
            

        elif output[0] == output[1] == output[2]:
            print(output[0] + " | " + output[1] + " | " + output[2])
            print("Congratulations! You won!")

            win = True
            tries += 1
            credit *= 3
            time.sleep(1)

        else:
            print(output[0] + " | " + output[1] + " | " + output[2])
            print("No match. Try again!")

            credit -= cost_per_play
            tries += 1

            time.sleep(1)

    total_score = credit
    print("You played " + str(tries) + " times.")
    print("You have " + str(credit) + " credits left.")
    print("Thank you for playing!")

    with open("scores.txt", "a") as f:
        f.write(f"{total_score} credits | {name} | {date_time}\n")

    while True:
        time.sleep(1.5)
        retry = input("Play again? ")

        if retry.lower() == "yes":
            break
        elif retry.lower() == "no":
            break
        else:
            print("Please enter yes or no.")

    if retry.lower() == "no":
        print("Goodbye!")
        break
 
with open("scores.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)

scores_data = []

for line in lines:
    parts = line.split("|")
    score_text = parts[0].strip()
    score_number = int(score_text.split()[0])
    scores_data.append([score_number, line])

scores_data.sort(reverse=True)

print("\nTop 10 Score Board:")
for i in range(min(10, len(scores_data))):
    print(scores_data[i][1].strip())
