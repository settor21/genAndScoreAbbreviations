# these functions are used to define the rules for suitable abbreviations
import re  # used in filtering out non-alphabets


def cleanText(word):
    # Regex expression used to filter out characters that are not
    # uppercase letters, spaces, or single quotes.
    # They are replaced with underscores
    word = re.sub(r"[^A-Z\s'À-ÖØ-Þ]", "_", word.upper())
    cleanedWord = ""  # empty string to hold the cleaned word

    # check if word is a compound word (separated)
    test = word.split()  # s
    if len(test) > 1:  # case for compound word

        for char in word.upper():  # for each character in the word
            if char.isalpha() or char == "'":  # if it's an alphabet or apostrophe
                cleanedWord += char
            else:
                cleanedWord += ' '  # Replace non-alphabetic characters with space
    else:
        cleanedWord = word  # word does not need any cleaning after filtering
    cleanedWord = cleanedWord.replace("'", "")  # Remove apostrophes
    return cleanedWord

# function which creates abbreviation


def createAbbreviations(word):
    # Clean the word using the previously defined cleanText function
    cleanedWord = cleanText(word)
    # Join spaces in the cleanedWord by
    # removing any existing whitespace using split
    cleanedWord = "".join(cleanedWord.split())
    abbreviations = []
    # create for only three letter words or more
    if len(cleanedWord) >= 3:
        firstLetter = cleanedWord[0]
        remainingLetters = cleanedWord[1:]

        # Iterate through the indices of remainingLetters
        # to form abbreviations from any two letters further away
        for i in range(len(remainingLetters)):
            for j in range(i + 1, len(remainingLetters)):
                abbreviation = firstLetter + \
                    remainingLetters[i] + \
                    remainingLetters[j]  # create the abbreviations
                # check if it's only uppercase alphabets (Will eliminate underscores)
                if re.match("^[A-Z]+$", abbreviation):
                    abbreviations.append(abbreviation)
    return abbreviations

# remove abbreviations which appear in more than one name


def removeDuplicateAbbreviations(dictionary):
    moreThanOne = []  # list to hold duplicates

    # Check for duplicate items in the dictionary values
    for key, value in dictionary.items():
        # Iterate through each item in the values
        for item in value:
            # Iterate through other key-value pairs in the dictionary
            for other_key, other_value in dictionary.items():
                # Check if the item is present in other values and in different keys
                if key != other_key and item in other_value:
                    moreThanOne.append(item)

    # Remove duplicate items from the dictionary values
    cleaned_dictionary = {}
    for key, value in dictionary.items():
        # Create a cleaned list without duplicate items
        cleaned_value = [item for item in value if item not in moreThanOne]
        # eliminate repeated correct self-duplicated values
        cleaned_dictionary[key] = list(set(cleaned_value))

    print("\n Duplicates Found:")
    print(list(set(moreThanOne)))

    return cleaned_dictionary

# will be used to track the position of letters, esp when split in an abbreviation during scoring
# creates an position mapping of all letters in the text
# Function to create an index for each character in a given text


def indexedText(text):
    text = text.upper()  # Convert text to uppercase
    indexedScores = {}  # Dictionary to store the index of each character
    words = text.split()  # Split the text into words to manage compound words
    for word in words:  # for aach entry
        for index, char in enumerate(word):  # for each letter and its index
            if char not in indexedScores:
                # Initialize an empty list for each character
                indexedScores[char] = []
            # Check if the character is the last in the word and
            # the word has more than one character
            if index == len(word) - 1 and len(word) > 1:
                # Append -1 to represent the last character in the word
                indexedScores[char].append(-1)
            else:
                # Append the index of the character
                indexedScores[char].append(index)
    return indexedScores  # Return the dictionary of indexed characters
