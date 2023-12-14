# this functions are used to define the rules for suitable abbreviations
import re


def cleanText(word):
    #clean single words with non-alphabets first
    # prepare compound words for cleaning
    cleanedWord = re.sub(r"[^A-Z\s']", "_", word.upper())
    cleanedWord = cleanedWord.replace("'", "")  # Remove apostrophes

    # Check if the cleanedWord contains spaces
    if ' ' in cleanedWord:
        words = cleanedWord.split()
        print(words)
        cleanedWord = ''
        for word in words:
            for char in word:
                if char.isalpha() or char == "'":
                    cleanedWord += char
                else:
                    cleanedWord += ' '
    return cleanedWord


def createAbbreviations(word):
    # Clean the word using the previously defined cleanText function
    cleanedWord = cleanText(word)
    # Join spaces in the cleanedWord
    cleanedWord = "".join(cleanedWord.split())
    abbreviations = []

    if len(cleanedWord) >= 3:
        firstLetter = cleanedWord[0]
        remainingLetters = cleanedWord[1:]

        for i in range(len(remainingLetters)):
            for j in range(i + 1, len(remainingLetters)):
                # Check if all letters in the abbreviation are alphabets
                abbreviation = firstLetter + \
                    remainingLetters[i] + remainingLetters[j]
                if re.match("^[A-Z]+$", abbreviation):
                    abbreviations.append(abbreviation)

    return abbreviations

# remove abbreviations which appear in more than one name


def removeDuplicateAbbreviations(dictionary):
    moreThanOne = []  # list to hold duplicates

    # Check for duplicate items in the dictionary values
    for key, value in dictionary.items():
        for item in value:
            for other_key, other_value in dictionary.items():
                if key != other_key and item in other_value:
                    moreThanOne.append(item)

    # Remove duplicate items from the dictionary values
    cleaned_dictionary = {}
    for key, value in dictionary.items():
        cleaned_value = [item for item in value if item not in moreThanOne]
        cleaned_dictionary[key] = cleaned_value

    print("\n Duplicates Found:")
    print(list(set(moreThanOne)))

    return cleaned_dictionary

# will be used to track the position of letters, esp when split in an abbreviation during scoring
# creates an position mapping of all letters in the text


def indexedText(text):
    text = text.upper()
    indexedScores = {}
    words = text.split()
    for word in words:
        for index, char in enumerate(word):
            if char not in indexedScores:
                indexedScores[char] = []
            # Check if the character is the last in the word
            if index == len(word) - 1 and len(word) > 1:
                indexedScores[char].append(-1)
            else:
                indexedScores[char].append(index)
    return indexedScores