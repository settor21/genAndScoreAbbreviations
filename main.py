from fileProcessors import *
from abbreviationRules import *
from scoreAbbreviations import *

def main():
    markingScheme = 'values.txt'
    wordsFile = getValidFileName()

    scoreCard = getMarkingScheme(markingScheme)
    wordList = getWordsForAbbreviations(wordsFile)

    print("Marking Scheme:")
    print(scoreCard)
    print("\nWords for Abbreviations:")
    print(wordList)
    # print("\nAbbreviations:")
    gradable = {}
    for word in wordList:
        abbreviations = createAbbreviations(word)
        gradable[word] = list(abbreviations)
    # print(gradable)
    uniqueGradables = removeDuplicateAbbreviations(gradable)
    # print("\nAbbreviation Scores:")
    scores = scoreEachAbbreviation(uniqueGradables, scoreCard)
    # print(scores)

    fileOutput = findLowestScoreAbbreviation(scores)
    print(fileOutput)
    outputResults(fileOutput, wordsFile)

if __name__ == "__main__":
    main()
