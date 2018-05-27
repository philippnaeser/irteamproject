java -jar ../RankLib-2.1-patched.jar -test base_tfidf.csv -metric2T NDCG@10 -gmax 2 -idv tfidf.base.txt

java -jar ../RankLib-2.1-patched.jar -test base_bm25.csv -metric2T NDCG@10 -gmax 2 -idv bm25.base.txt

java -jar ../RankLib-2.1-patched.jar -test base_bm25_alt.csv -metric2T NDCG@10 -gmax 2 -idv bm25_alt.base.txt

java -jar ../RankLib-2.1-patched.jar -test base_unigram.csv -metric2T NDCG@10 -gmax 2 -idv unigram.base.txt

java -jar ../RankLib-2.1-patched.jar -test base_cosine.csv -metric2T NDCG@10 -gmax 2 -idv cosine.base.txt

java -jar ../RankLib-2.1-patched.jar -test base_fasttext.csv -metric2T NDCG@10 -gmax 2 -idv fasttext.base.txt

java -jar ../RankLib-2.1-patched.jar -test base_word2vec.csv -metric2T NDCG@10 -gmax 2 -idv word2vec.base.txt