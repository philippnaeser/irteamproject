java -Xmx6g -jar RankLib-2.1-patched.jar -train train.csv -ranker 1 -metric2t NDCG -gmax 3 -validate dev.csv -save pairwise.ndcg.model

java -jar RankLib-2.1-patched.jar -load pairwise.ndcg.model -test test.csv -metric2T NDCG -gmax 3 -idv pairwise.ndcg.eval.txt
