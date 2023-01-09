BOT = print('Welcome to my restaurant! How can I help you today?')

def display_options():
  print("**OPTIONS TO CHOOSE BY** ")
  print("Can I make reservations?") 
  print("What is on the menu today?")
  print("Can I place my order?")
  print("Nothing! Thank you!")

def user_selection():
  selection = input(': ')
  if selection == "Can I make reservations?":
    print('We will schedule a reservation for the most available date. Thank you for coming!')
  if selection == 'What is on the menu today?':
    print('We currently have some regular congee, a omelette with melted cheese on top, and our steak special.')
  if selection == "Can I place my order?":
    order = input('What would you like to order?')
    print("Got it! Ill send out your food soon, thank you for coming  here and enjoy your meals when it arrives.")
  if selection == "Nothing! Thank you!":
    print("Ok then, thanks for visiting anyways and have a great day!")

  while selection != user_selection():
    selection = input('Would you like anything else?')

display_options()
user_selection()