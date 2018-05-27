java -Xmx6g -jar RankLib-2.1-patched.jar -train train.csv -ranker 1 -epoch 20 -layer 2 -node 50 -metric2t NDCG@10 -gmax 2 -validate dev.csv -save pairwise.ranknet.ndcg10.model

java -jar RankLib-2.1-patched.jar -load pairwise.ranknet.ndcg10.model -test test.csv -metric2T NDCG@10 -gmax 2 -idv pairwise.ranknet.ndcg10.eval.txt

