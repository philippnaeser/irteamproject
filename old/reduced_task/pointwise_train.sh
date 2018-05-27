java -Xmx6g -jar RankLib-2.1-patched.jar -train train.csv -ranker 0 -metric2t NDCG -gmax 3 -validate dev.csv -save pointwise.ndcg.model
