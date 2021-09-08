import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def whitespace():
    print('\n')

def define(word):
    whitespace()
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no:  " % get_close_matches(word, data.keys()))[0]
        if yn == "Y":
            whitespace()
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            whitespace()
            return "This word does not exist, please try again."
        else:
            return "Sorry, that entry is not recognised."
    else:
        return "This word does not exist, please try again."

word = input("Enter a word to get the definition: ")

output = define(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)