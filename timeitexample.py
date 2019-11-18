import timeit

## timeit usage example
# print(timeit.timeit('1+3', number=500000))


# input_list = range(100)
# 
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return True
# 
# xyz = (i for i in input_list if div_by_five(i))
# 
# xyz = [i for i in input_list if div_by_five(i)]


## print(timeit.timeit('''
## 
## input_list = range(100)
## 
## def div_by_five(num):
##     if num % 5 == 0:
##         return True
##     else:
##         return True
## 
## xyz = list((i for i in input_list if div_by_five(i)))
## 
## xyz = [i for i in input_list if div_by_five(i)]
## 
## ''', number=5000))

##note you need to include the whole script in timeit
