java -Xmx6g -jar RankLib-2.1-patched.jar -train train.csv -ranker 1 -layer 2 -node 50 -epochs 20 -metric2t NDCG -gmax 2 -validate dev.csv -save pairwise_RankNet_0.model
java -jar RankLib-2.1-patched.jar -load pairwise_RankNet_0.model -test test.csv -metric2T NDCG -gmax 2 -idv pairwise_RankNet_0.model.eval.txt

