#1

#list_1 = ['name', 'age', '1', '19']
#def divide_list_and_reverse(l):
#    polovina = len(l)//2
#    part_1 = list(reversed(l[0:polovina]))
#    part_2 = list(reversed(l[polovina:]))
#    part_1.extend(part_2)
#    return part_1
#print(divide_list_and_reverse(list_1))

#2

# def fibonacci(n):
#    if n in(1,2):
#         return 1
#    return fibonacci(n-1) + fibonacci(n-2)

# for i in range(1,11):
#     print(fibonacci(i),end=',')

#3
# def plus(a,b):
#     return a+b

# def minus(a,b):
#     return a-b

# def print_plus_minus(c,d):
#     print(plus(c,d),minus(c,d))
# print_plus_minus(3,4)

#4
# name = input('name_file: ')
# def create_file(n):
#     file_name = f'{n}.txt'
#     with open(file_name,'w') as f:
#         f.write('File Created!!!')
#     return 'File Created'
# f1 = create_file(name)
# print(f1)



#5
# from random import choice
# def gen_number():
#     main_part = '0444'
#     for i in range(6):
#         main_part+=choice(['1','4','5','7','9','0'])
#     return main_part
# print(gen_number())

#6
# l1 = [1,2,3,4,5,6,7,8,9,10,11,12]
# def odd_numbers(l):
#     return [n for n in l if n%2!=0]
# print(odd_numbers(l1))

#7
# s1 = {1,2,3,4,5,6,7,8,9}
# def set_deleter(s):
#     if len(s)==1:
#         s.pop()
#         return s
    
#     s.pop()
#     return set_deleter(s)

# print(set_deleter(s1))


