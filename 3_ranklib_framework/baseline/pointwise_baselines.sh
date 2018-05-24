java -Xmx6g -jar ../RankLib-2.1-patched.jar -train train_tfidf.csv -ranker 0 -metric2t NDCG@1000 -gmax 2 -validate dev_tfidf.csv -save point.base.tfidf.model
java -jar ../RankLib-2.1-patched.jar -load point.base.tfidf.model -test test_tfidf.csv -metric2T NDCG@1000 -gmax 2 -idv tfidf.point.base.txt

java -Xmx6g -jar ../RankLib-2.1-patched.jar -train train_bm25.csv -ranker 0 -metric2t NDCG@1000 -gmax 2 -validate dev_bm25.csv -save point.base.bm25.model
java -jar ../RankLib-2.1-patched.jar -load point.base.bm25.model -test test_bm25.csv -metric2T NDCG@1000 -gmax 2 -idv bm25.point.base.txt

java -Xmx6g -jar ../RankLib-2.1-patched.jar -train train_bm25_alt.csv -ranker 0 -metric2t NDCG@1000 -gmax 2 -validate dev_bm25_alt.csv -save point.base.bm25_alt.model
java -jar ../RankLib-2.1-patched.jar -load point.base.bm25_alt.model -test test_bm25_alt.csv -metric2T NDCG@1000 -gmax 2 -idv bm25_alt.point.base.txt

java -Xmx6g -jar ../RankLib-2.1-patched.jar -train train_unigram.csv -ranker 0 -metric2t NDCG@1000 -gmax 2 -validate dev_unigram.csv -save point.base.unigram.model
java -jar ../RankLib-2.1-patched.jar -load point.base.unigram.model -test test_unigram.csv -metric2T NDCG@1000 -gmax 2 -idv unigram.point.base.txt

java -Xmx6g -jar ../RankLib-2.1-patched.jar -train train_cosine.csv -ranker 0 -metric2t NDCG@1000 -gmax 2 -validate dev_cosine.csv -save point.base.cosine.model
java -jar ../RankLib-2.1-patched.jar -load point.base.cosine.model -test test_cosine.csv -metric2T NDCG@1000 -gmax 2 -idv cosine.point.base.txt

java -Xmx6g -jar ../RankLib-2.1-patched.jar -train train_fasttext.csv -ranker 0 -metric2t NDCG@1000 -gmax 2 -validate dev_fasttext.csv -save point.base.fasttext.model
java -jar ../RankLib-2.1-patched.jar -load point.base.fasttext.model -test test_fasttext.csv -metric2T NDCG@1000 -gmax 2 -idv fasttext.point.base.txt

java -Xmx6g -jar ../RankLib-2.1-patched.jar -train train_word2vec.csv -ranker 0 -metric2t NDCG@1000 -gmax 2 -validate dev_word2vec.csv -save point.base.word2vec.model
java -jar ../RankLib-2.1-patched.jar -load point.base.word2vec.model -test test_word2vec.csv -metric2T NDCG@1000 -gmax 2 -idv word2vec.point.base.txt