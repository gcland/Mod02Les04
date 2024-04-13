item_list = ['Apple', 'Water', 'Sword', 'Gloves', 'Gold', 'Cloth']
import random
item_select = random.choice(item_list)
print(item_select) #To check if correct guess works. Remove for real use.

for x in range(0, 100):
    guess = input("Guess the item from the list: Apple, Water, Sword, Gloves, Gold, or Cloth. ")
    if guess == item_select:
        if x > 1:
            print("Correct,", guess +"!")
            print("It took you ", str(x+1) + " guesses!")
        elif x == 0:
            print("Correct,", guess +"!")
            print("It took you ", str(x+1) + " guess!")
        break
    elif x == 2:
        print("C'mon; there are only 6 items to choose from! The correct answer was,", guess +". Game over!")
        break
    else:
        print("Not", guess + ". Try again!")
        
