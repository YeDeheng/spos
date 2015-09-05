:: C:\Python27\python main.py input_raw.txt input2tagger.txt
:: usage: stanford-postagger model textFile
::  e.g., stanford-postagger models\english-left3words-distsim.tagger sample-input.txt
:: pre-tag the input text using stanford Tagger

java -mx300m -cp "stanford-postagger-3.5.2.jar;" edu.stanford.nlp.tagger.maxent.MaxentTagger -sentenceDelimiter newline -tokenize false -model models\english-bidirectional-distsim.tagger -textFile input.txt > output.txt