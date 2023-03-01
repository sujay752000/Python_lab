g_lst = [-1, 2, 4, 5, -4, -6, -10]
word = "sujay prasad"

positive_lst = [i for i in g_lst if i > 0]
print(positive_lst)

sqr_lst = [i**2 for i in g_lst]
print(sqr_lst)

vwl_lst = [i for i in word if i in "aeiou"]
print(vwl_lst)

ord_lst = [ord(i) for i in word]
print(ord_lst)
