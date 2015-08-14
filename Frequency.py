class Frequency:
    '''Frequency Class'''
    def __init__(self, word: 'str'):
        self.word = word
        self.frequency = 0
    def __init__(self,word,frequency):
        self.word = word
        self.frequency = frequency
    def getText(self):
        return self.word

    def getFrequency(self):
        return self.frequency

    def incrementFrequency(self):
        self.frequency +=1

    def setFrequency(self,frequency_count):
        self.frequency = frequency_count
    def toString(self):
        return self.word + ":" + self.frequency
