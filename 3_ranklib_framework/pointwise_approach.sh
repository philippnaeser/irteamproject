java -Xmx6g -jar RankLib-2.1-patched.jar -train train.csv -ranker 0 -metric2t NDCG@1000 -gmax 2 -validate dev.csv -save pointwise.ndcg1000.model

java -jar RankLib-2.1-patched.jar -load pointwise.ndcg1000.model -test test.csv -metric2T NDCG@1000 -gmax 2 -idv pointwise.ndcg1000.eval.txt

