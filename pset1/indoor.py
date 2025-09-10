# Function that takes an input and uses .lower() Method in output
statement = input("What is on your mind: ")

def indoor_voice(str):
    print(statement.lower(), "\n")

indoor_voice(statement)