from compareBigramTypes import compare_Bigram_Types as bigramTypes
from compareWordTypes import compare_Word_Types as wordTypes

x = [item for item in input("Input in the specific sequence [\"file1\", \"file2\", U/B, Y/N, threshold]:").split(", ")]


content1 = open(x[0].strip('"'), 'r')
content1 = content1.readlines().pop()

content2 = open(x[1].strip('"'), 'r')
content2 = content2.readlines().pop()


def plagiarismDetector(file1, file2, analysisType, norm, threshold):

    global plagiarism_quotient

    if analysisType == 'U':
        plagiarism_quotient = wordTypes(list(file1), list(file2), norm)

    elif analysisType == 'B':
        plagiarism_quotient = bigramTypes(file1, file2, norm)

    print(f'The plagiarism quotient is {plagiarism_quotient}')

    if plagiarism_quotient >= float(threshold):
        return "Exit code: 1 - The content has been plagiarised"
    else:
        return "Exit code: 0 - The content is deemed to be fine"


print(f'The result is: {plagiarismDetector(content1, content2, x[2], x[3], x[4])}')
