text = "I am Sujay Prasad I am sujay"
text_lst = text.split(" ")
word_dict = {}
for i in text_lst:
    if i in text:
        word_dict.update({i: text.count(i)})

for key , val in word_dict.items():
    print(f"{key} -> {val}")
    