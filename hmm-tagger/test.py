
from collections import namedtuple, OrderedDict

sequences=[("ram","raj"),("siri","siri"),("siri","ram","siri")]

unigram_counts = {}

for i, sentence in enumerate(sequences):
    for j, y in enumerate(sentence):
        if y in unigram_counts:
            unigram_counts[y] += 1
        else:
            unigram_counts[y] = 1

        
    
print(unigram_counts)