
import gensim


#### note this is a usage example . Will not make sense as corpus and labels . For demo purpose .

#### Assume your corpus will have good relations

#### label_dict contains words and labels

label_dict = {'crow': 'bird' ,

			'cow': 'animal' ,

			'parrot': 'bird' ,

			'fox': 'animal' ,

			'bus': 'vehicle' ,

			'train': 'vehicle'}


import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

## Importtant this works well for category

senetences = ['Crow will fly' , 'peackok will dance' , 'bus carry people' , 'train is faster']

sentences_tokens = []

for sent in sentences:
	sentences_tokens.append(sent.split())

model = gensim.models.Word2Vec_Supervised(sentences_tokens, size=100, window=15, hs=0, negative=5,  iter=5,  min_count=2, workers=cpu_count(), label_dict = label_dict )

cPickle.dump( model, open('save_model.pkl', 'wb'), protocol=2)

