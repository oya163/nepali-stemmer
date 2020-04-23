# Nepali Stemmer

This is simple Nepali stemmer. It iteratively separates out the suffixes (postpositions) until no more separation can be processed. The algorithm is based on hindi-stemmer.

## Features:
 - Iterative separation
 - Handles the postposition attached with punctuations carefully
     - Example: नेपाललाई, -> नेपाल लाई,
 - Checks with Nepali dictionary

## How to run

    python nep_stemmer.py


## To-do:
- [ ] Word transformation when stemmed
- [ ] IR evaluation


## References:
 - Suffix list: https://github.com/birat-bade/NepaliStemmer
 - Nepali Dictionary : https://github.com/PraveshKoirala/stemmer
 - Algorithm : https://github.com/sainimohit23/hindi-stemmer
