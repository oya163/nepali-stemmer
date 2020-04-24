# Nepali Stemmer

This is a simple Nepali stemmer. It iteratively separates out the suffixes (postpositions) until no more separation can be processed. The algorithm is based on hindi-stemmer.

## Features:
 - Iterative separation
 - Handles the postposition attached with punctuations carefully
     - Example: नेपाललाई, -> नेपाल लाई,
 - Cross-verification with Nepali dictionary

## How to run

    >>> from nepali_stemmer.stemmer import NepStemmer
    >>> nepstem = NepStemmer()
    >>> nepstem.stem("नेपालको एमाले पार्टीका झोले, मण्डलेहरु अमेरिका आउने रे !")                                                                                                      
    
    'नेपाल को एमाले पार्टी का झोले, मण्डले हरु अमेरिका आउने रे !'


## To-do:
- [ ] Word transformation with stemming process
- [ ] IR evaluation


## References:
 - Suffix list: https://github.com/birat-bade/NepaliStemmer
 - Nepali Dictionary : https://github.com/PraveshKoirala/stemmer
 - Algorithm : https://github.com/sainimohit23/hindi-stemmer


## Contact
oyashi
