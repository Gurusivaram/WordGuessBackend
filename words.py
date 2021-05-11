from nltk.corpus import wordnet
from wordModel import *
from typing import List
from re import search
import random
from wordList import *


def getResultForWord() -> List[Word]:
    list = []
    i = 0
    while i < 5:
        randomIndex = getRandomWithinRange(wordList)
        currentWord = wordList[randomIndex]
        currentWordData = wordnet.synsets(currentWord)
        if(len(currentWordData) != 0):
            currentWordDataRandomIndex = getRandomWithinRange(currentWordData)
            for relatedWord in currentWordData[currentWordDataRandomIndex].lemmas():
                if relatedWord.name() != currentWord and not search(currentWord, relatedWord.name()) and not search("-,_", relatedWord.name()):
                    if(relatedWord.antonyms()):
                        relatedWordWordAntonymsDataRandomIndex = getRandomWithinRange(
                            relatedWord.antonyms())
                        list.append(Word(currentWord, relatedWord.name().replace(
                            '_', ' '), relatedWord.antonyms()[relatedWordWordAntonymsDataRandomIndex].name()).__dict__)
                    else:
                        temp = wordnet.synsets(
                            wordList[getRandomWithinRange(wordList)])
                        while len(temp) == 0:
                            temp = wordnet.synsets(
                                wordList[getRandomWithinRange(wordList)])
                        tempRandomIndex = getRandomWithinRange(temp)
                        relatedWordLemmaRandomIndex = getRandomWithinRange(
                            temp[tempRandomIndex].lemmas())
                        list.append(Word(currentWord, relatedWord.name().replace(
                            '_', ' '), temp[tempRandomIndex].lemmas()[relatedWordLemmaRandomIndex].name()).__dict__)
                    i += 1
                    break
    return list


def getRandomWithinRange(range):
    return random.randint(0, len(range)) % len(range)
