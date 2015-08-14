import Utilities
import Frequency
import sys

def computeTwoGramFrequencies(words: '[string]') ->str:
    '''
    Given a list of words computes the frequency of each two word
    combination.
    '''
    if words == None:
        return []
    twoGramFrequencies = []
    twoGramDict = create2GramDict(words)
    for val in sorted(twoGramDict.values(), key = lambda x: (-x.getFrequency(),x.getText()), reverse=False):
        twoGramFrequencies.append(val)

    return twoGramFrequencies
    

def create2GramDict(words: '[string]') -> dict:
    '''
    Computes and returns dictionary of {2Gram: count}
    '''
    length = len(words)
    twoGramDict = {}
    for index in range(1,length):
        twoGram = words[index-1] + " " + words[index]
        if twoGram in twoGramDict.keys():
            twoGramDict[twoGram].incrementFrequency()
        else:
            frequency = Frequency.Frequency(twoGram,1)
            twoGramDict[twoGram] = frequency
    return twoGramDict

def main(filename: 'str') -> None:
    '''
    Computes two word combinations and outputs them and their
    frequency
    '''
    words = Utilities.tokenizeFile(filename)
    frequencies = computeTwoGramFrequencies(words)
    Utilities.printFrequencies(frequencies)

if __name__=='__main__':
    main(sys.argv[1])
