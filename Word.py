import io
import random

class Words:

    def __init__(self,filename):
        self.filename = filename
        self.palabras = []
        self.load()
    
    
    def load(self):
        with io.open(self.filename, 'r', encoding='utf-8') as f:
            for line in f:
                self.palabras.append(line.strip())
            
        
    def get_palabra(self):
        return random.choice(self.palabras)
            
    def get_password(self, size):
        password = ''
        for i in range(size):
            palabra = self.get_palabra()
            password += palabra[0].upper()+palabra[1:]
        password += str(random.randint(0,9))+str(random.randint(0,9))
        return password

if __name__ == '__main__':
    word = Words('palabras.txt')
    print(word.get_password(2))