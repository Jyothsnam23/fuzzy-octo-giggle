# def num(n1,n2):
#     sum = n1*n2
#     return(sum)

# result = num(2,3)
# print(result)


# def sum_thrice(x,y,z):
#     sum = x+y+z

#     if x == y == z:
#       sum = sum *3
#     return sum

# print (sum_thrice(1,2,3))
# print (sum_thrice(3,3,3))


# # Exception handling 

# try:
#     numerator = int(input("Enter numerator:"))
#     demoninator = int(input("Enter denominator: "))

#     result = numerator/demoninator
#     print(result)

# except:
#     print ("demoninator cannot be zero. please try again")

# print ("program ends")


# Lambda

# xyz = lambda x,y,z : x+y+z

# print(xyz(2,2,2))


# Collections Counter

   
# from collections import Counter
# a = "aaaaabbbbbcccccdddddd"
# my_counter = Counter(a)
# print(my_counter)
# print(my_counter.items())

# Collection namedtuple

# from collections import namedtuple
# Point = namedtuple('Point', 'x,y')
# pt = Point(2,7)
# print(pt)

# # Just to get the values 
# from collections import namedtuple
# Point = namedtuple('Point', 'x,y')
# pt = Point(2,7)
# print(pt.x, pt.y)

# Collection orderdict
# Ordereddict will remember the order of the dictionarty.
# from collections import OrderedDict
# ordered_dict = {}
# ordered_dict['e'] = 5
# ordered_dict['d'] = 4
# ordered_dict['c'] = 3
# ordered_dict['b'] = 2
# ordered_dict['a'] = 1
# print(ordered_dict)


# from collections import OrderedDict
# ordered_dict = OrderedDict()
# ordered_dict['e'] = 5
# ordered_dict['d'] = 4
# ordered_dict['c'] = 3
# ordered_dict['b'] = 2
# ordered_dict['a'] = 1
# print(ordered_dict)


# Collections Defaultdict


# from collections import defaultdict
# d = defaultdict(float)
# d['a'] =1
# d['b'] =2
# print(d['c'])


# Collection deque

# from collections import deque
# d = deque()

# d.append(1)
# d.append(2)

# d.appendleft(3)
# print(d)

# d.pop()
# print(d)








