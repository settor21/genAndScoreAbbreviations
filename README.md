# genAndScoreAbbreviations
This program generates and scores abbreviations from a list of names, represented as single lines of text in a file. It consists of four files: 
 - **main.py** to run the program to score and generate abbreviations
 -  **fileProcessors.py** to read values from the scorecard(value.txt) and the list of names (user inputs a text file)
 -  **abbreviationRules.py** to convert the names to uppercase, filter out non-alphabets and generate three-letter abbreviations
 -  **scoreAbbreviations.py** to score the non-duplicate abbreviations based on the scorecard, first and last letter index values.
