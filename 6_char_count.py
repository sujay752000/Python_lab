word = input("Enter a word : ")

word_dict = {}

for i in word:
    word_dict.update({i: word.count(i)})

print(word_dict)