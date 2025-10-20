# with open('fruit.txt','w') as f:
#     f.write('Apples, 10\n')
#     f.write('Peaches, 5\n')
#
# with open('fruit.txt','a') as f:
#     f.write('Cherries, 60\n')
#     f.write('Apricots, 25\n')

# with open('fruit.txt','r') as f:
#     # print(f.read())
#     # print(f.tell())
#     # print(f.seek(0))
#     # print(f.readlines())
#     # f.seek(0)
#     fruit_data = {}
#     line = f.readline()
#     while line:
#         fruit, count = line.strip().split(', ')
#         fruit_data[fruit] = int(count)
#         line = f.readline()
#     print(fruit_data)
#
# with open('fruit.txt', 'w+') as f:
#     new_fruit = ['Watermelon, 1\n', 'Pineapple, 1\n', 'Fish (How did it get here?!), 7\n', 'Mushrooms (?!), 10\n']
#     f.writelines(new_fruit)
#     print(f.tell())
#     f.seek(0)
#     print(f.readlines())
#
# with open ('fruit.txt') as f:
#     data = f.readlines()
# print(data)


# sum = lambda a, b: a + b
# print(sum)
#
# data = [1, 2, 3,4]
#
# new_data = map(lambda x: x*2, data)
# print(list(new_data))
#
# odd_even = map(lambda x: 'even' if x%2 == 0 else 'odd', data )
# print(list(odd_even))

# my_list = [4, 6, 3, 1, 2, 7, 0, 5]
# my_list.sort()
# print(my_list)
#
# my_list.sort(reverse=True)
# print(my_list)
#
# result = sorted((10, 30 ,20 ,70, 60, 40, 50))
# print(result)
#
# pairs = [('First', 1), ('Third', 3), ('Second', 2), ('Fifth', 5), ('Fourth', 4)]
# print(sorted(pairs))
#
# a=sorted(pairs, key=lambda pair: pair[1])
# print(a)

# print(sorted('python'))

fruit_data = {}
sor