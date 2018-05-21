java -Xmx6g -jar RankLib-2.1-patched.jar -train train.csv -ranker 0 -metric2t NDCG -gmax 3 -validate dev.csv -save pointwise.ndcg.model

java -jar RankLib-2.1-patched.jar -load pointwise.ndcg.model -test test.csv -metric2T NDCG -gmax 3 -idv pointwise.ndcg.eval.txt

