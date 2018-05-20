https://sourceforge.net/p/lemur/wiki/RankLib%20How%20to%20use/

Here you can find other ranking methods and evaluations.

First, run putting_it_all_together to create train.csv and test.csv (train.csv is 500MB, so i did not include it in github)
To train and evaluate a ranklib model, simply open a shell here and run train (pointwise or pairwise) first, then test accordingly (for windows, you may want to copy the command to the powershell,
if sh is not enabled on your computer). Since this is a Java framework, make sure you have set JAVA_HOME in your PATH Environment Variable.

Note that both trainings can run quite a while, especially the pairwise ranker.
