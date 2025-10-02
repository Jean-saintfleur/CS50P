greeting = input("What is your current mood: ")

def greet(text):
    # Replaces each emojies
    text = text.replace(":)", "😀")
    text = text.replace(":(", "☹️")
    return text

result = greet(greeting)
print(result)