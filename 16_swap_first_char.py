word1 = input("Enter first word : ")
word2 = input("Enter second word : ")

new_word = ""

new_word = new_word + word2[0] + word1[1: len(word1)] + " " + word1[0] + word2[1: len(word2)]
print(new_word)