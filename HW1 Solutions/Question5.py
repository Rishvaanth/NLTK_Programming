from compareBigramTypes import compare_Bigram_Types

x = [item for item in input("Input in the specific sequence [\"s1\", \"s2\", Y/N]:").split(", ")]
x[0] = x[0].strip('"')
x[1] = x[1].strip('"')
print(f'Computing the solution based on the parameters.....\n {compare_Bigram_Types(x[0], x[1], x[2])}')
