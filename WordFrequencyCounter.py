#!/usr/bin/python
import Utilities
import Frequency
import sys

def computeWordFrequencies(words: '[string]') -> list:
    '''
    Computes frequency of tokens
    '''
    if words == None:
        return
    frequencies = []
    frequencyDict = createFrequencyDict(words)
    #sorts the values by descending frequency, alphabetically
    for val in sorted(frequencyDict.values(), key = lambda x: (-x.getFrequency(),x.getText()), reverse=False):
        frequencies.append(val)
    return frequencies

def createFrequencyDict(words: '[string]') -> dict:
    '''
    Creates a dict of Frequencies
    '''
    frequencyDict = {}
    for word in words:
        if word in frequencyDict.keys():
            frequencyDict[word].incrementFrequency()
        else:
            frequency = Frequency.Frequency(word, 1)
            frequencyDict[word] = frequency
    return frequencyDict

def main(filename: 'str') -> None:
    '''
    Computes word tokens and outputs them and their
    frequency
    '''
    words = Utilities.tokenizeFile(filename)#input file name here
    #make sure it's in the same directory
    frequencies = computeWordFrequencies(words)
    Utilities.printFrequencies(frequencies)

if __name__=='__main__':
    main(sys.argv[1])
