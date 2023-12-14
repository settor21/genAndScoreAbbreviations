import os  # helps in checking if file exists in directory

# this function stores the default letter scores by reading from a file into a dictionary.


def getMarkingScheme(file_path):
    markingScheme = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                key, value = line.split()
                markingScheme[key] = int(value)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError:
        print(f"Error: Invalid data format in file {file_path}")
    return markingScheme

# this function gets the words to be used for the abbreviation scoring and stores
# them in a set. Set was chosen over list to prevent duplicates.


def getWordsForAbbreviations(file_path):
    words = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                word = line.strip()
                if not word:
                    raise ValueError(
                        "Error: Words should be on different lines in the file.")
                words.add(word)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError as ve:
        print(ve)
    return words


# outputs the name used for the abbreviation and its
# lowest scored abbrev to a file
def outputResults(fileOutput, wordsFile):
    # get the actual name of the file without the .txt using splitext searches
    wordsFile = os.path.splitext(wordsFile)[0]
    output_file_name = f"amediku_{wordsFile}_abbrevs.txt"
    if os.path.exists(output_file_name):
        # clear contents of pre-existing files
        open(output_file_name, 'w').close()

    with open(output_file_name, 'w', encoding='utf-8') as output_file:
        for word, abbreviations in fileOutput.items():
            output_file.write(f"{word}\n")  # the name used
            for abbreviation, score in abbreviations.items():
                if score is None or score == float('inf'):
                    output_file.write("  \n")  # print blanks
                else:

                    output_file.write(f"{abbreviation}\n")

    print(f"Results have been written to {output_file_name}")


def getValidFileName():
    while True:
        wordsFile = input(
            "Enter the text file (must be in the same directory): ")
        if os.path.isfile(wordsFile):
            return wordsFile
        else:
            print(
                f"The file {wordsFile} does not exist in the current directory. Please enter a valid filename.")
