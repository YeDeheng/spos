SET root=.
ECHO %root%

:: %1% : <input file>
:: %2% : <output file>

java -Xmx2g -Xms2g -jar %root%\classes\posTagTwitter.jar ^
      edu.cmu.cs.lti.ark.ssl.pos.SemiSupervisedPOSTagger ^
      --trainOrTest test ^
      --testSet %1% ^
      --numLabeledSentences 2147483647 ^
      --maxSentenceLength 200 ^
      --useGlobalForLabeledData ^
      --useStandardMultinomialMStep  ^
      --useStandardFeatures ^
      --regularizationWeight 0.707 ^
      --regularizationBias 0.0 ^
      --initialWeightsLower -0.01 ^
      --initialWeightsUpper 0.01 ^
      --iters 1000 ^
      --printRate 100 ^
      --runOutput %root%\%2% ^
      --execPoolDir %root%\tmp ^
      --modelFile %root%\model\twitter_crf.model ^
      --useDistSim ^
      --useNames
