#!/bin/bash

java -cp stanford-postagger-3.5.2.jar edu.stanford.nlp.tagger.maxent.MaxentTagger -sentenceDelimiter newline -tokenize false -model models/english-bidirectional-distsim.tagger -textFile $1  > $2
