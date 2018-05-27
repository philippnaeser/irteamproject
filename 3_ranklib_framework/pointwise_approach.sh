java -Xmx6g -jar RankLib-2.1-patched.jar -train train.csv -ranker 0 -metric2t NDCG@10 -gmax 2 -validate dev.csv -save pointwise.ndcg10.model

java -jar RankLib-2.1-patched.jar -load pointwise.ndcg10.model -test test.csv -metric2T NDCG@10 -gmax 2 -idv pointwise.ndcg10.eval.txt

