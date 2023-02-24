
class Letter:

    def __init__(self, letter):
        self.letter = letter
        self.dic = {}

    def __repr__(self):
        self.dic = str(self.dic)
        self.dic = self.dic.replace('{', '')
        self.dic = self.dic.replace('}', '')
        self.dic = self.dic.replace("'", '')

        return f'{self.dic}'

    def encode(self, word):
        lista = []
        for i in range(len(word)):
            if word[i] == self.letter:
                lista.append(i+1)
        self.dic[self.letter] = lista
        # print(type(self.dic))
        # nueva = str(self.dic)
        # print(type(nueva))
        # nueva = nueva.replace('{', '[')
        # nueva = nueva.replace('}', ']')
        # print(nueva)