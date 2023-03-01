word = "ssuusssjjjaaayyyssss"
# print(word[0], end="")
# for i in range(1, len(word)):
#     if word[i] == word[0]:
#         print("$", end="")
#     else:
#         print(word[i], end="")
#

first_char = word[0]

new_word = "" + first_char

for i in range(1, len(word)):
    if word[0] == word[i]:
        new_word = new_word + "$"

    else:
        new_word = new_word + word[i]

print(new_word)
