# Import necessary modules for file processing, abbreviation rules, and scoring
from fileProcessors import *
from abbreviationRules import *
from scoreAbbreviations import *

# Main function to execute the abbreviation scoring process


def main():
    markingScheme = 'values.txt'  # Specify the file containing the marking scheme values
    wordsFile = getValidFileName()  # Prompt the user to enter the text file with words

    # Retrieve the marking scheme values
    scoreCard = getMarkingScheme(markingScheme)
    wordList = getWordsForAbbreviations(wordsFile)  # Retrieve the set of words

    # Display the marking scheme and words for abbreviations
    print("Marking Scheme:")
    print(scoreCard)
    print("\nWords for Abbreviations:")
    print(wordList)

    gradable = {}  # Initialize a dictionary to store words and their corresponding abbreviations
    for word in wordList:
        # Generate abbreviations for each word
        abbreviations = createAbbreviations(word)
        # Store unique and sorted abbreviations for each word
        gradable[word] = sorted(list(abbreviations))

    uniqueGradables = removeDuplicateAbbreviations(
        gradable)  # Remove duplicate abbreviations
    print()
    print(uniqueGradables)  # Display words with unique abbreviations

    print("\nAbbreviation Scores:")
    scores = scoreEachAbbreviation(
        uniqueGradables, scoreCard)  # Score each abbreviation
    for name, abbreviations in scores.items():
        print(name)
        for abbrev, score in abbreviations.items():
            # Display each abbreviation and its score
            print(f"{abbrev} - {score}")
        print()
    # Find the lowest scored abbreviation for each word
    fileOutput = findLowestScoreAbbreviation(scores)
    outputResults(fileOutput, wordsFile)  # Output the results to a file


# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
