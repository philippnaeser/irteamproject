java -jar RankLib-2.1-patched.jar -load pointwise.ndcg1000.model -test test.csv -metric2T NDCG@1000 -gmax 2 -idv pointwise.ndcg.eval.txt

java -jar RankLib-2.1-patched.jar -load pointwise.ndcg1000.model -test test.csv -metric2T NDCG@10 -gmax 2s -idv pointwise.ndcg.eval.txt
