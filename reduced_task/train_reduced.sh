java -Xmx6g -jar RankLib-2.1-patched.jar -train train.csv -ranker 0 -metric2t NDCG -gmax 3 -validate dev.csv -norm zscore -save rank_lib.3.2.1.ndcg.model
