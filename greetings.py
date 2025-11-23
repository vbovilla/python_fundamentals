# define function

# function which uses 'global' variable
# def greeting():
#     print('Hello ', name)

# function which uses 'local' variable
def greeting(name):
    print('Hello', name)


# name = input('Enter your name:\n')
# greeting()

# Main program
name1 = input('Enter your name:\n')
greeting(name1)


name2 = input('Enter your name:\n')
greeting(name2)
