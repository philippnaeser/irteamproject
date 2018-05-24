java -Xmx6g -jar ../RankLib-2.1-patched.jar -train ../train.csv -ranker 0 -metric2t NDCG@1000 -gmax 2 -validate ../dev.csv -feature tfidf.txt -save base.tfidf.model
java -jar ../RankLib-2.1-patched.jar -load base.tfidf.model -test ../test.csv -feature tfidf.txt -metric2T NDCG@1000 -gmax 2 -idv tfidf.base.txt

java -Xmx6g -jar ../RankLib-2.1-patched.jar -train ../train.csv -ranker 0 -metric2t NDCG@1000 -gmax 2 -validate ../dev.csv -feature bm25.txt -save base.bm25.model
java -jar ../RankLib-2.1-patched.jar -load base.bm25.model -test ../test.csv -feature bm25.txt -metric2T NDCG@1000 -gmax 2 -idv bm25.base.txt

java -Xmx6g -jar ../RankLib-2.1-patched.jar -train ../train.csv -ranker 0 -metric2t NDCG@1000 -gmax 2 -validate ../dev.csv -feature bm25_alt.txt -save base.bm25_alt.model
java -jar ../RankLib-2.1-patched.jar -load base.bm25_alt.model -test ../test.csv -feature bm25_alt.txt -metric2T NDCG@1000 -gmax 2 -idv bm25_alt.base.txt

java -Xmx6g -jar ../RankLib-2.1-patched.jar -train ../train.csv -ranker 0 -metric2t NDCG@1000 -gmax 2 -validate ../dev.csv -feature unigram.txt -save base.unigram.model
java -jar ../RankLib-2.1-patched.jar -load base.unigram.model -test ../test.csv -feature unigram.txt -metric2T NDCG@1000 -gmax 2 -idv unigram.base.txt

java -Xmx6g -jar ../RankLib-2.1-patched.jar -train ../train.csv -ranker 0 -metric2t NDCG@1000 -gmax 2 -validate ../dev.csv -feature cosine.txt -save base.cosine.model
java -jar ../RankLib-2.1-patched.jar -load base.cosine.model -test ../test.csv -feature cosine.txt -metric2T NDCG@1000 -gmax 2 -idv cosine.base.txt

java -Xmx6g -jar ../RankLib-2.1-patched.jar -train ../train.csv -ranker 0 -metric2t NDCG@1000 -gmax 2 -validate ../dev.csv -feature fasttext.txt -save base.fasttext.model
java -jar ../RankLib-2.1-patched.jar -load base.fasttext.model -test ../test.csv -feature fasttext.txt -metric2T NDCG@1000 -gmax 2 -idv fasttext.base.txt

java -Xmx6g -jar ../RankLib-2.1-patched.jar -train ../train.csv -ranker 0 -metric2t NDCG@1000 -gmax 2 -validate ../dev.csv -feature word2vec.txt -save base.word2vec.model
java -jar ../RankLib-2.1-patched.jar -load base.word2vec.model -test ../test.csv -feature word2vec.txt -metric2T NDCG@1000 -gmax 2 -idv word2vec.base.txt