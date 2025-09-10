# prompts user for input and uses .replace method to print statement
str = input("Your statement: ")

def playback(i):
    print(str.replace(" ", "..."))

playback(str)