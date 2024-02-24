x = [2, 4, 6, 8, 10, 12]
cut_1 = x[-1:2:-2]
cut_2 = x[::-2]
#cut_3 = x[0::0] ValueError: slice step cannot be zero
cut_4 = x[1::3]
cut_5 = x[0]
print(cut_1, cut_2, cut_4, cut_5)