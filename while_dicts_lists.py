# moving items from one list to another

unconfirmed_users = ['bob', 'jen', 'alice']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f'verifying user: {current_user.title()}')
    confirmed_users.append(current_user)

# display all the confirmed users now
print("\nThe following users have been confirmed and verified: ")
for x in confirmed_users:
    print(x.title())

# remove all instances of specific values from a list
pets = ['dog', 'cat', 'mouse', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# fill a dictionary with user inputs
responses = {}
polling_active = True # set a flag to indicate polling is active

while polling_active:
    name = input("\nwhat is your name?: ")
    response = input("which mountain would you like to climb someday?: ")
    responses[name] = response

    repeat = input("Would you like to le another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- poll results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")