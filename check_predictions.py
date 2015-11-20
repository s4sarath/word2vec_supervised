########### How to check the classification or labels "
#### So we need to check , how the words in the corpus has been classified . This can be done as follows


import cPickle
from scipy import spatial

#### Load the trained model

model = cPickle.load(open('saved_model.pkl'))


def check_labels( word ):
  res = {}
  for word_ in model.vocab:
      
      res[word_] = 1.0 - spatial.distance.cosine( model[word] , model.syn1neg[model.vocab[word_].index])
  return sorted( res.items() , key = lambda x: x[1] , reverse = True)
  

### example usage to find the label of word crow

label_crow = check_labels( 'crow' )

print label_crow

##### You can see the labels with their closeness ( vector similarity measure )




  
  
