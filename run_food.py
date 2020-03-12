from food import *


ordering_food = ''
items_of_food = []

print('')
print(10 * '=', 'ORDERING FOOD & DRINKS', 10 * '=')
print("1. Lets Make An Order")
print("2. Lets View The List Of Food")
print('')

user_input = input("Would You Like To Make An Order? Y/N \n")

while True:

    if user_input == 'Y':
        print("Good! What Would You Like.")

    elif user_input == 'N':
        print("I See, You Aren't Hungry. Have A Good Day")
        break

    print(input("Lets Make An Order (1)."))
    print(input("Here Are The List Of Food (2)."))

    elif user_input == '1':
        print('What Would You Like To Order')

    elif user_input == '2':
        print('')

  # user_input = input("Would You Like To Order? Y/N \n")
        # if user_input == 'y' or user_input == 'Y':
        #     ordering_food = input("What Would You Like To Order: \n")
        #     items_of_food.append(ordering_food)
        #
        # elif user_input == 'n':
        #     print("Enjoy Your Meal")
        #     break
        #
        # else:
        #     print("Maybe Come Again When You're Feeling Peckish")