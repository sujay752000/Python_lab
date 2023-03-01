word = input("Enter a word")
length = len(word)
if word[-3:] == "ing":
    print(word[-length: -3] + "ly")
else:
    print(word + "ing")