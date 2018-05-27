java -Xmx6g -jar RankLib-2.1-patched.jar -train train.csv -ranker 6 -metric2t NDCG@10 -gmax 2 -validate dev.csv -save listwise_lambdaMART_0.model

java -jar RankLib-2.1-patched.jar -load listwise_lambdaMART_0.model -test test.csv -metric2T NDCG@10 -gmax 2 -idv listwise_lambdaMART_0.model.eval.txt

