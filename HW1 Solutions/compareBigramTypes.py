import nltk
from nltk import pos_tag, word_tokenize


def compare_Bigram_Types(str1, str2, norm):
    # Tokenization is performed inside the function here to prevent additional steps to de-tokenize or pass more
    # arguments
    x1 = (pos_tag(word_tokenize(str1)))  # removing quotations
    x2 = (pos_tag(word_tokenize(str2)))  # same as above for the next sentence
    twoWordPOS = 0

    # Bigramming

    strbig1 = (list(nltk.bigrams(x1)))
    strbig2 = (list(nltk.bigrams(x2)))

    for i in strbig1:
        for j in strbig2:
            print(f'Comparing {i} and {j} \n')
            if i == j:
                twoWordPOS = twoWordPOS + 1
                print(f'Match found!\n \n')

    if norm == 'Y':
        return twoWordPOS / ((len(str1) + len(str2)) / 2)
    elif norm == 'N':
        return twoWordPOS
    else:
        return "Invalid parameter. should be Y or N for normalization (case sensitive)"
