from abbreviationRules import *
import itertools

def scoreEachAbbreviation(gradable, markingScheme):
    scores = {}

    for word, abbreviations in sorted(gradable.items()):
        wordScores = {}
        for abbreviation in abbreviations:
            cleanedText = cleanText(word)
            dividedWord = cleanedText.split()
            indexedWord = indexedText(cleanedText)
            if abbreviation in wordScores:
                abbreviationScore = calculateScoreForAllCombinations(
                    abbreviation, indexedWord, markingScheme, dividedWord)
                wordScores[abbreviation] = abbreviationScore
            else:
                abbreviationScore = calculateScore(
                    abbreviation, indexedWord, markingScheme, dividedWord)
                wordScores[abbreviation] = abbreviationScore
        scores[word] = wordScores
    return scores

def calculateScore(abbreviation, indexedWord, markingScheme, word):
    firstLetter = abbreviation[0]
    secondLetter = abbreviation[1]
    thirdLetter = abbreviation[2]

    # Makes it easy to score each distinct letter
    def getScore(letter):
        index_values = indexedWord.get(letter, [3])
        index_value = index_values.pop(0) if index_values else 3

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

    firstLetterScore = getScore(firstLetter)
    secondLetterScore = getScore(secondLetter)
    thirdLetterScore = getScore(thirdLetter)

    return firstLetterScore + secondLetterScore + thirdLetterScore

def calculateScoreForAllCombinations(abbreviation, indexedWord, markingScheme, word):
    firstLetter = abbreviation[0]
    secondLetter = abbreviation[1]
    thirdLetter = abbreviation[2]

    def getAllScores(letter):
        index_values = indexedWord.get(letter, [3])
        index_value = index_values.pop(0) if index_values else 3

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

    all_combinations = itertools.product(
        indexedWord[firstLetter], indexedWord[secondLetter], indexedWord[thirdLetter]
    )

    min_score = float('inf')

    for combination in all_combinations:
        firstLetterScore = getAllScores(firstLetter)
        secondLetterScore = getAllScores(secondLetter)
        thirdLetterScore = getAllScores(thirdLetter)

        total_score = firstLetterScore + secondLetterScore + thirdLetterScore
        min_score = min(min_score, total_score)

    return min_score

def findLowestScoreAbbreviation(scores):
    lowestScoredAbbreviation = {}

    for word, wordScores in sorted(scores.items()):
        lowest_score = float('inf')  # Initialize with a very high score
        lowest_score_abbreviations = []

        for abbreviation, score in sorted(wordScores.items()):
            if score < lowest_score:
                lowest_score = score
                lowest_score_abbreviations = [abbreviation]
            elif score == lowest_score:
                lowest_score_abbreviations.append(abbreviation)

        if word not in lowestScoredAbbreviation:
            lowestScoredAbbreviation[word] = {}

        lowestScoredAbbreviation[word][' '.join(
            lowest_score_abbreviations)] = lowest_score

    return lowestScoredAbbreviation
