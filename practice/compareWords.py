from nltk import pos_tag, word_tokenize

s1 = "Hello and welcome to phasmophobia."
s2 = "Welcome to rust."
sc1=(pos_tag(word_tokenize(s1)))
print('\n')
sc2=(pos_tag(word_tokenize(s2)))

print(sc1)
print('\n')
print(sc2)
print(len(sc1))
lsc1 = len(sc1)
firstfirst = sc1[0]
secondfirst = sc2[0]
print(firstfirst, secondfirst)
print(firstfirst == secondfirst)
lsc2 = len(sc2)
print(lsc2)
print(sc1[1])
count = 0

for i in sc1:
    for j in sc2:
        print(f'Comparing {i} and {j}')
        if i==j:
            count = count+1
            print("Matched!")

print(count)

