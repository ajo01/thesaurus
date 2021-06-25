import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        userInput = input("Did you mean %s instead? Enter Y for yes and N for no." %
                          get_close_matches(word, data.keys())[0])
        if userInput == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif userInput == 'N':
            return 'The word does not exist.'
        else:
            return "We don't understand your query."
    else:
        return 'The word does not exist. Please double check it.'


word = input("Enter word: ")

print(translate(word))
