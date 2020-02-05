def decision_making():
    x = input("Please enter a number between 1,4 and 3:")
    if x == 1:
        print('You type "I"')
    elif x == 4:
        print('You type "LIKE"')
    elif x == 3:
        print('You type "YOU"')
    else:
        print("Oops! pick number from 1,4 and 3 only!")
decision_making()