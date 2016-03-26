item = ['asdsad', 'qweqwe', 234]
item1, item2, price = ['asdsad', 'qweqwe', 234]
print (item[0])
print (price)


def dropfirst_last(grades):
    first, *middle, last = grades
    avg = sum(middle)/len(middle)
    print(avg)

dropfirst_last([12,23,344,55623,324])
dropfirst_last([12,23,55623,324])
dropfirst_last([12,23,344,324])
