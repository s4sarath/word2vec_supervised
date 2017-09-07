import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim.models import Word2Vec_Supervised


########## A Small Demo 
### Better to provide min_count = 1 ( otheriwse make sure your labels
## occur more than min_count .) .

### Labels must provide in a dictionary format . key : [list of l
### Multiple labels are also possible . Even single label , it should be in 
### a list



sentences = [ ["skirt"  , "shirt" , "pants"] ,
			  ["lipstick" , "top" , "scarf"] ]

label_dict = { "skirt": ["women_category"] ,
			   "shirt": ["men_category"] , 
			   "lipstick":["women_category"],
			   "top":["women_category" , "men_category"] ,
			   "scarf":["women_category"]}

model = Word2Vec_Supervised( sentences , min_count=1, window=5, hs=0 , negative = 7 , label_dict = label_dict , workers = 4)

##### Once the model is trained , you can find the top categories by

model.most_similar_category(["skirt"])