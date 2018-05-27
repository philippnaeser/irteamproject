java -Xmx6g -jar RankLib-2.1-patched.jar -train train.csv -ranker 6 -metric2t NDCG@10 -gmax 2 -validate dev.csv -save listwise.lambda.ndcg10.model

java -jar RankLib-2.1-patched.jar -load listwise.lambda.ndcg10.model -test test.csv -metric2T NDCG@10 -gmax 2 -idv listwise.lambda.ndcg10.eval.txt

