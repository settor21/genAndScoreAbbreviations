# genAndScoreAbbreviations
This program generates and scores abbreviations from a list of names, represented as single lines of text in a file. It consists of four files: 
 - **main.py** to run the program to score and generate abbreviations
 -  **fileProcessors.py** to read values from the scorecard(value.txt) and the list of names (user inputs a text file)
 -  **abbreviationRules.py** to convert the names to uppercase, filter out non-alphabets and generate three-letter abbreviations
 -  **scoreAbbreviations.py** to score the non-duplicate abbreviations based on the scorecard, first and last letter index values.

The program reads each line as a phrase or word hence the list of names need to be on multiple lines, as shown in **trees.txt**.
The program was tested using words(compound (-), words with foreign letters, long words, words shorter than three) and phrases. 

The final output of the program will be stored as
Cold
CLD
for each name with generated abbreviations in the file amediku_fileName_abbrevs.txt where CLD is the least scored generated abbreviation
