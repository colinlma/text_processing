import Frequency
import Utilities
import sys

def computePalindromeFrequencies(words:'[string]') -> list:
    '''
    Computes and returns palindromes found in words
    '''
    frequencies = []
    palindromeDict = {}
    for index in range(0, len(words)):
        currentWords=''
        longestPalindrome = ''
        for i in range(index, len(words)):
            currentWords= currentWords + words[i] + ' '
            longestPalindrome= getLongestPalindrome(currentWords, longestPalindrome)
        if longestPalindrome in palindromeDict.keys():
            palindromeDict[longestPalindrome].incrementFrequency()
        else:
            if(longestPalindrome != ''):
                frequency = Frequency.Frequency(longestPalindrome, 1)
                palindromeDict[longestPalindrome] = frequency
    for val in sorted(palindromeDict.values(), key = lambda x: (-x.getFrequency(),x.getText()), reverse=False):
        frequencies.append(val)
    return frequencies

            
def getLongestPalindrome(currentWords:'string', longestPalindrome: 'string') ->str :
    '''
    Computes the longest palindrome in currentWords
    '''
    testWords=currentWords.replace(' ','')
    if(len(testWords)<2):
        return longestPalindrome
    begin = 0
    end = len(testWords)-1
    while(begin < end):
        if(testWords[begin] != testWords[end]):
            return longestPalindrome
        begin +=1
        end -=1
    return currentWords

def main(filename: 'str') -> None:
    '''
    Finds the palindromes in the file and prints the number of occurences of them.
    '''
    words = Utilities.tokenizeFile(filename)
    frequencies = computePalindromeFrequencies(words)
    Utilities.printFrequencies(frequencies)

if __name__=='__main__':
    main(sys.argv[1])
