'''
    Simple Nepali stemmer
    
    Date: 04/23/2020
    
    References:
        Suffix : https://github.com/birat-bade/NepaliStemmer
        Nepali Dictionary : https://github.com/PraveshKoirala/stemmer
        Algorithm : https://github.com/sainimohit23/hindi-stemmer
'''

import re
import sys
from root import *

'''
    Reference: https://github.com/PraveshKoirala/stemmer
'''

class NepStemmer:
    def __init__(self, shabdakosh='', suffix_path=''):
        self.nep_dict = nep_dictionary(shabdakosh)
        self.suffix_path = suffix_path
        self.suffixes = self.get_suffix()
        
        
    def get_suffix(self):        
        # Create a dictionary by the length of suffix
        with open(self.suffix_path, 'r') as suff_file:
            suffixes = {}
            for row in suff_file.read().splitlines():
                stem_len = len(list(row))
                if stem_len not in suffixes:
                    suffixes[stem_len] = [row]
                else:
                    suffixes[stem_len] += ([row])

        return suffixes


    # Devanagari range \u0900-\u097F
    # Alphanumeric range \w
    def clean_text(self, text, chars=None):
        puncts = "()\"#/@;:<>{}`+-=~|!?,'।॥’–"
        if chars == None:
            text = re.findall(r"[\w\u0900-\u097F]+|["+puncts+"]", text)
        else:
            text = re.findall(r"[\w\u0900-\u097F]+|[" +chars+ "()\"#/@;:<>{}`+=~|!?,'।॥]", text)
        return text


    '''
        Reference: https://github.com/sainimohit23/hindi-stemmer
    '''
    def nep_stem(self, word, clean=True, chars=None):
        if clean == True:
            # Return the text with punctuation separated
            word = self.clean_text(word, chars)

        # if text cleaned, return the added the punctuation at the end
        # process only first part of cleaned_text
        punct=''
        if clean:
            if len(word) > 1:
                punct = ''.join(word[1:])
            ans = word[0]
            core_word = word[0]
        else:
            ans = word
            core_word = word

        bl = False

        # Do not stem the word which is from
        # Nepali dictionary
        if ans in self.nep_dict:
            # Reattach the punctuation
            return ans+punct if len(word)>1 else ans

        # Iteratively process the stem
        for L in 9, 8, 7, 6, 5, 4, 3, 2:
            if len(core_word) > L + 1:
                for suf in self.suffixes[L]:
                    if core_word.endswith(suf):
                        ans = core_word[:-L] + ' ' + core_word[-L:]
                        bl =True
            if bl == True:
                break

        # Might be required later for unit length suffixes
    #     if bl == True:
    #         for suf in suffixes[1]:
    #             if ans.endswith(suf):
    #                 ans = nep_stem(ans)

        # Might be required later for transformation in suffixes
    #     for suf in special_suffixes:
    #         if ans.endswith(suf):
    #             l = len(suf)
    #             ans = ans[:-l]
    #             ans += dict_special_suffixes[suf] 

        # Reattach the punctuation
        return ans+punct if len(word)>1 else ans



if __name__=="__main__":
    s = NepStemmer(shabdakosh="./files/shabdakosh-words.txt", suffix_path='./files/suffix.txt')

    test_string = """बीपी कोइराला स्वास्थ्य विज्ञान प्रतिष्ठान धरानमा गरिएको स्वाब परीक्षणमा भोजपुरका २६ वर्षीय पुरुषमा कोरोना संक्रमण देखिएको डा. अधिकारीले जानकारी दिए।

यसअघि आजै जनकपुरका १४ वर्षीय बालक र उदयपुरकी ५५ वर्षीया महिलामा पनि कोरोना संक्तमण देखिएको थियो। त्यस्तै आजै संक्रमितमध्ये ३ जना निको भएर घर फर्किएका छन्। बिहीबार साँझसम्म कोरोना संक्रमणपछि निको हुनेको संख्या १० पुगेको छ। """
    
    print("Test string : {}\n".format(test_string))

    result = []
    for each in test_string.split():
        result.append(s.nep_stem(each, clean=True))

    print("Output string : {}".format(' '.join(result)))
