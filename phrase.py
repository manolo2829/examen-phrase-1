from word import Word 

class Phrase:

    def __init__(self):
        self.phrase = []
    def __repr__(self):
        return f'{self.phrase}'

    def encode(self, text):
        lista = text.split(' ')
        for word in lista:
            newWord = Word(word)
            newWord.encode()
            self.phrase.append(newWord)