from nltk import pos_tag, word_tokenize
from compareWordTypes import compare_Word_Types

x = [item for item in input("Input in the specific sequence [\"s1\", \"s2\", Y/N]:").split(", ")]
x[0] = (pos_tag(word_tokenize(x[0].strip('"'))))  # removing quotations
x[1] = (pos_tag(word_tokenize(x[1].strip('"'))))  # same as above for the next sentence

print(f'Computing the solution based on the parameters.....\n {compare_Word_Types(x[0], x[1], x[2])}')
