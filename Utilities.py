import Frequency
import re
def tokenizeFile(file_path: 'str') -> list:
    '''
    Splits the text file into tokens and returns them as a list
    '''
    file = open(file_path, 'r')
    word_list = []
    #currentMAXURL = 0
    #totalText = 0
    for line in file:
        line = re.split(r'\W+', line)
        for word in line:
            if word != "":
                word = word.lower()
                word_list.append(word)
    return word_list

def printFrequencies(frequencies: '[Frequency') -> None:
    '''
    Prints all the Frequency objects in frequencies
    '''
    if(frequencies == None or frequencies[0]== None):
        return []
    totalCount = getTotalCount(frequencies)
    uniqueCount = len(frequencies)
    print("Total item count: " + str(totalCount))
    print("Unique item count: " + str(uniqueCount))
    print()
    for frequency in frequencies:
        print(frequency.getText() + " " + str(frequency.getFrequency()))

def getTotalCount(frequencies: '[Frequency]') -> int:
    '''
    Calculates count of all the Frequency objects, including duplicates
    '''
    totalCount = 0
    for frequency in frequencies:
        totalCount += frequency.getFrequency()
    return totalCount


def merge_sort(frequencies: '[Frequency]') -> list:
    '''
    Merge sort implentation for Frequency class, not used in the code (anymore)
    '''
    length = len(frequencies)
    if(length == 1):
        return frequencies
    array1 = frequencies[:length//2]
    array2 = frequencies[length//2:length]
    array1 = merge_sort(array1)
    array2 = merge_sort(array2)
    array3 = merge(array1, array2)
    return array3

def merge(array1: '[Frequency]', array2: '[Frequency]') -> list:
    '''
    Part of merge sort implementation, not used in the code (anymore)
    '''
    i = 0
    j = 0
    length = len(array1) + len(array2)
    array3=[]
    while(i < len(array1) and j < len(array2)):
        if(array1[i].getFrequency() > array2[j].getFrequency()):
            array3.append(array1[i])
            i=i+1
        elif(array1[i].getFrequency() == array2[j].getFrequency()):
            if(array1[i].getText() < array2[j].getText()):
                array3.append(array1[i])
                i=i+1
            else:
                array3.append(array2[j])
                j=j+1
        else:
            array3.append(array2[j])
            j+=1
    if(i < len(array1)):
        for i2 in range(i, len(array1)):
            array3.append(array1[i2])
    else:
        for j2 in range(j, len(array2)):
            array3.append(array2[j2])
    return array3

            
