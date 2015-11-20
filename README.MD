1. Go the directory where gensim is installed

	In my case /Library/Python/2.7/site-packages/gensim/models

	Edit __init__.py and add from .word2vec_supervised import Word2Vec_Supervised

2. Compile cython code by
	sudo python setup_w2v_supevised.py build_ext

			or

	sudo python setup_w2v_supevised.py build_ext --inplace

3. If word2vec_inner_supervised.so is not created

	do 

	cc -bundle -undefined dynamic_lookup -arch x86_64 -arch i386 -Wl,-F. build/temp.macosx-10.10-intel-2.7/word2vec_inner_supervised.o -o ~/Desktop/word2vec_inner_supervised.so

	From Desktop copy it to the current directory

	cp ~/Desktop/word2vec_inner_supervised.so .

4. Run test.py 

	If everything is fine 'Success' will get print


5. Sample usage and necessary parameters can be found in sample_supervise.py




 
