class Formatter:
    def __init__(self, word):
        self.word = word
        self.capitalize = False

class Sentence(list):
    def __init__(self, plain_text):
        for word in plain_text.split(" "):
            self.append(Formatter(word))

    def __str__(self):
        sentence = []
        
        for word in self:
            if word.capitalize:
                sentence.append(word.word.upper())
            else:
                sentence.append(word.word)
                
        return " ".join(sentence)
        