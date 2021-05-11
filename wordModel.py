import json 

class Word:
    def __init__(self, word, relatedWord, notRelatedWord):
        self.word = word
        self.relatedWord = relatedWord
        self.notRelatedWord = notRelatedWord
        self.correctAnswer = relatedWord