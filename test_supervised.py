
try:
	from gensim.models.word2vec_inner_supervised import train_sentence_sg_mod, train_sentence_sg, train_sentence_sg_categ, train_sentence_sg_categ_nogil, train_sentence_cbow, FAST_VERSION
	print 'Success'
except:
	print 'Failed to load train_sentence_sg_mod from gensim.models.word2vec_inner_supervised '

