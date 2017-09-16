import indicoio
import pickle
import codecs
import numpy as np

inputText = 'This is a sentence'
indicoio.config.api_key = 'ab83001ca5c484aa92fc18a5b2d6585c'

categories = ['education', 'nutrition']
categorySentences = []
for category in range(4):
    counter = 0
    categorySentences.append([])
    while(True):
        try:
            filename = categories[category] + 'Samples' + str(counter) + '.txt'
            with codecs.open(filename, 'r', 'UTF-8') as infile:
                sentences = infile.read().split('.')
                categorySentences[-1] = categorySentences[-1] + sentences
                print(categorySentences[-1])
            counter += 1
        except:
            break
#print(indicoio.text_features(["There are so many things you can learn from text.", "Bitches ain't shit but hoes and tricks"]))