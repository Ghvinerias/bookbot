word_count = 0
lettterSet = set()
input_file = 'books/frankenstein.txt'


def readFileContents(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
    return file_contents

def readFileWordCount(file_contents):
    count = 0
    for i in file_contents.split():
        count += 1
    return count

def collectLetters(letter):
    letterOccuranceSet = set()
    for i in letter:
        if i.isalpha():
            letterOccuranceSet.add(i.lower())
    letterOccuranceDict = dict.fromkeys(letterOccuranceSet, 0)
    enemies_dict = {}
    for l in letter:
        if l.isalpha():
            if l.lower() in letterOccuranceDict:
                letterOccuranceDict[l.lower()] += 1
            else:
                letterOccuranceDict[l.lower()] = 1
    return letterOccuranceDict

def main():
    data = readFileContents(input_file)
    word_count = readFileWordCount(data)
    letterOccuranceDictionary = collectLetters(data)
    print("--- Begin report of", input_file, "---")
    print(word_count, "words found in the document")
    print("")
    for letter in letterOccuranceDictionary:
        occuranceNumber = letterOccuranceDictionary[letter]
        print(f"The '{letter}'  character was found {occuranceNumber} times")
main()
