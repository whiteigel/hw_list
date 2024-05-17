num = 1
limit = 100
even_list = []
while num <= limit:
    if num % 2 == 0:
        even_list.append(num)
    num += 1
print(even_list)

num = 1
limit = 100
even_list = []
while num <= limit:
    if num % 2 == 0:
        sqr = num ** 2
        even_list.append(sqr)
    num += 1
print(even_list)
