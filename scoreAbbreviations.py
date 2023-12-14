from abbreviationRules import *  # text formatting functions used
import itertools  # use product method to generate all possible combinations of self-repeated abbreviations


def scoreEachAbbreviation(gradable, markingScheme):
    """
    Scores each abbreviation for a given word based on the 
    specified rules and score card.

    Args:
    gradable (dict): A dictionary containing words as keys
    and their non-duplicate abbreviations as values.
    markingScheme (dict): A dictionary containing distinct letter scores 
    from values.txt.

    Returns:
    dict: A dictionary containing word scores with their corresponding abbreviations.
    """
    scores = {}  # hold scores for this text batch
    # loop through each gradable abbreviation key-value pair when sorted
    for word, abbreviations in sorted(gradable.items()):
        wordScores = {}  # dictionary to hold all word scores
        for abbreviation in abbreviations:  # for each abbrev
            cleanedText = cleanText(word)  # filter the original name
            dividedWord = cleanedText.split()  # used to check indexing during test
            # identify all text positions
            indexedWord = indexedText(cleanedText)
            # check if the abbreviation can be created from the same word more than once and has been scored already
            if abbreviation in wordScores:
                abbreviationScore = calculateScoreForAllCombinations(
                    abbreviation, indexedWord, markingScheme, dividedWord)
                wordScores[abbreviation] = abbreviationScore
            else:  # abbreviation is generated from word once
                abbreviationScore = calculateScore(
                    abbreviation, indexedWord, markingScheme, dividedWord)
                # assign the abbreviation and its score to wordScores
                wordScores[abbreviation] = abbreviationScore
        # assign the dictionary of abbreviation scores for the word to scores
        scores[word] = wordScores
    return scores

# function to swap indexes of first two elements in list


def swapFirstTwo(lst):
    if len(lst) >= 2:  # parameter check
        lst[0], lst[1] = lst[1], lst[0]


def calculateScore(abbreviation, indexedWord, markingScheme, word):
    """
    Calculates the score for a given abbreviation based on the 
    specified rules and marking scheme.

    Args:
    abbreviation (str): The abbreviation to be scored.
    indexedWord (dict): The indexed representation of the cleaned word.
    markingScheme (dict): The dictionary containing alphabet scores.
    word (list): Reference for the indexedWord. Used in debugging.

    Returns:
    int: The total score for the abbreviation.
    """
    # store each letter from abbreviation as variable
    firstLetter = abbreviation[0]
    secondLetter = abbreviation[1]
    thirdLetter = abbreviation[2]

    # Makes it easy to score each distinct letter
    def getScore(letter):
        # Obtain index values for the letter and pop the first value
        index_values = indexedWord.get(letter, [3])
        index_value = index_values.pop(0) if index_values else 3

        # Swap next two positions if first and third letter repeats
        if index_value == 0 and firstLetter == thirdLetter and firstLetter != secondLetter:
            swapFirstTwo(index_values)

        # specified rules for scoring letters
        if index_value == 0:
            return 0
        elif index_value == -1:
            if letter == 'E':
                return 20
            else:
                return 5
        elif index_value == 1:
            return 1 + markingScheme.get(letter, 0)
        elif index_value == 2:
            return 2 + markingScheme.get(letter, 0)
        else:
            return 3 + markingScheme.get(letter, 0)
    # score each letter
    firstLetterScore = getScore(firstLetter)
    secondLetterScore = getScore(secondLetter)
    thirdLetterScore = getScore(thirdLetter)
    # return the sum
    return firstLetterScore + secondLetterScore + thirdLetterScore


def calculateScoreForAllCombinations(abbreviation, indexedWord, markingScheme, word):
    """
    Calculates the score for all repeated combinations of a given abbreviation 
    based on the specified rules and marking scheme. eg. ZAZ Zanzamaamzama

    Args:
    abbreviation (str): The abbreviation to be scored.
    indexedWord (dict): The indexed representation of the cleaned word.
    markingScheme (dict): The dictionary containing alphabet scores.
    word (list): Reference for the indexedWord. Used in debugging.

    Returns:
    int: The total score for the abbreviation.
    """
    firstLetter = abbreviation[0]
    secondLetter = abbreviation[1]
    thirdLetter = abbreviation[2]
    # function to determine a letter score using the specified rules

    def getAllScores(letter):
        index_values = indexedWord.get(letter, [3])
        index_value = index_values.pop(0) if index_values else 3
        # rules specified
        if index_value == 0:
            return 0
        elif index_value == -1:
            if letter == 'E':
                return 20
            else:
                return 5
        elif index_value == 1:
            return 1 + markingScheme.get(letter, 0)
        elif index_value == 2:
            return 2 + markingScheme.get(letter, 0)
        else:
            return 3 + markingScheme.get(letter, 0)
        
    # Generate all combinations of indices for each letter 
    # using itertools.product for faster computation
    all_combinations = itertools.product(
        indexedWord[firstLetter], indexedWord[secondLetter], indexedWord[thirdLetter]
    )

    # arbitrary minimum score for quick computation
    min_score = float('inf')
    
    # Loop through each combination and calculate scores
    for combination in all_combinations:
        firstLetterScore = getAllScores(firstLetter)
        secondLetterScore = getAllScores(secondLetter)
        thirdLetterScore = getAllScores(thirdLetter)

        total_score = firstLetterScore + secondLetterScore + thirdLetterScore
        # compare each iterations score and get the minimum
        min_score = min(min_score, total_score) 
    return min_score


def findLowestScoreAbbreviation(scores):
    lowestScoredAbbreviation = {}

    for word, wordScores in sorted(scores.items()):
        lowest_score = float('inf')  # Initialize with a very high score
        lowest_score_abbreviations = []
        for abbreviation, score in sorted(wordScores.items()):
            # Check if the score is lower than the current lowest score
            if score < lowest_score:
                # Update the lowest score
                lowest_score = score
                lowest_score_abbreviations = [abbreviation]
            elif score == lowest_score: # check for similar scores and add them
                lowest_score_abbreviations.append(abbreviation)                
        # Update the lowestScoredAbbreviation dictionary with the final result
        if word not in lowestScoredAbbreviation:
            lowestScoredAbbreviation[word] = {}
        #join multiple abbreviations or the single abbreviation with lowest score into screen 
        lowestScoredAbbreviation[word][' '.join(
            lowest_score_abbreviations)] = lowest_score  # add them to the dictionary
    return lowestScoredAbbreviation #return the final dictionary