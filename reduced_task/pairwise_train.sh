java -Xmx6g -jar RankLib-2.1-patched.jar -train train.csv -ranker 1 -metric2t NDCG -gmax 3 -validate dev.csv -save pairwise.ndcg.model
