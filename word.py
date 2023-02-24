from letter import Letter

class Word:
    
    def __init__(self, word):
        self.word = word
        self.lista = []
    def __repr__(self,):
        return f'{self.lista}'
    

    def encode(self):
        lista = list(self.word)
        lista2 = []
        lista3= []
        for letter in lista:
            if(not letter in lista3):
                lista3.append(letter)
                newLetter = Letter(letter)
                newLetter.encode(lista)
                lista2.append(newLetter)
        self.lista = lista2