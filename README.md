# Nepali Stemmer

This is a simple Nepali stemmer. It iteratively separates out the suffixes (postpositions) until no more separation can be processed. The algorithm is based on hindi-stemmer.

## Features:
 - Iterative separation
 - Handles the postposition attached with punctuations carefully
     - Example: नेपाललाई, -> नेपाल लाई,
 - Basic text cleaning
 - Cross-verification with Nepali dictionary

## How to install
    pip install -r requirements.txt
    
    pip install nepali-stemmer

## How to run

    from nepali_stemmer.stemmer import NepStemmer
    nepstem = NepStemmer()
    nepstem.stem("नेपालको एमाले पार्टीका झोले, मण्डलेहरु अमेरिका आउने रे !")
    
    'नेपाल को एमाले पार्टी का झोले, मण्डले हरु अमेरिका आउने रे !'


## Deployment

A simple flask based web app [deployment](https://nepali-stemmer.herokuapp.com/)



## To-do:
- [ ] Word transformation with stemming process
- [ ] IR evaluation
- [ ] Code-mixed data


## References:
 - Suffix list: https://github.com/birat-bade/NepaliStemmer
 - Nepali Dictionary : https://github.com/PraveshKoirala/stemmer
 - Algorithm : https://github.com/sainimohit23/hindi-stemmer


## Contact
Email: [oyashi](mailto:oyeshsin@hotmail.com)

Note: Project created during COVID-19 quarantine out-of-boredom and necessity
