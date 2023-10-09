# Name:Varun Patil
# Batch:B3
# Roll:43
# Title:-

########################################################################################

import gensim
from gensim import corpora
from gensim.utils import simple_preprocess
from gensim import corpora


text1 = ["""I want to go to school . I am going to school now ."""]

tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)

print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)

g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text1])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text1]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')

print("TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])

####################################################################################

# output:-
# {'.': 0, 'I': 1, 'am': 2, 'go': 3, 'going': 4, 'now': 5, 'school': 6, 'to': 7, 'want': 8}
# Bag of Words :  [[(0, 2), (1, 2), (2, 1), (3, 1), (4, 1), (5, 1), (6, 2), (7, 3), (8, 1)]]
# Dictionary : 
# [['be', 1], ['better', 1], ['but', 1], ['can', 1], ['excellent', 1], ['food', 1], ['is', 1], ['service', 1], ['the', 2]]
# [['food', 1], ['is', 1], ['service', 1], ['the', 2], ['always', 1], ['and', 1], ['delicious', 1], ['loved', 1]]
# [['food', 1], ['service', 1], ['the', 2], ['and', 1], ['mediocre', 1], ['terrible', 1], ['was', 2]]

