import random

# create a new dictionary
new_dict = {}
# get the int input of a user to add their total number of friends
num = int(input("Enter the number of friends joining (including you):"))
# if int input is greater than 0 keep going
if num > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    # input the name of your friends, and they will be added to a dictionary name:0
    for i in range(num):
        name = input()
        new_dict[name] = 0

    # input the bill total
    bill = int(input("Enter the total bill value:"))

    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')

    # if 'yes' is chosen here the random module will choose a name from the dictionary
    # the name chosen will be excluded from the dictionary and the bill total would be
    # divided by num - 1. The dictionary will look like name:new value
    if lucky.lower() == 'yes':
        luck_name = random.choice(list(new_dict.keys()))
        print(f"{luck_name} is the lucky one!")
        new_dict = {key: round(bill / (num - 1), 2) for (key, value) in
                    new_dict.items() if key not in {luck_name}}

        # I add the chosen key back with a value of 0
        new_dict[luck_name] = 0

        print(new_dict)

    else:
        print("No one is going to be lucky")
        for dictionary in new_dict:
            new_dict.update({dictionary: round(bill / num, 2)})
        print(new_dict)
# if int input is less than or equal to 0 print this value
else:
    print('No one is joining for the party')
