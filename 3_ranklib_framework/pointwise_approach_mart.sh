java -Xmx6g -jar RankLib-2.1-patched.jar -train train.csv -ranker 0 -tree 500 -leaf 100 -shrinkage 0.2 -metric2t NDCG@10 -gmax 2 -validate dev.csv -save pointwise.mart.ndcg10.model

java -jar RankLib-2.1-patched.jar -load pointwise.mart.ndcg10.model -test test.csv -metric2T NDCG@10 -gmax 2 -idv pointwise.mart.ndcg10.eval.txt

