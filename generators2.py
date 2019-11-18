input_list = [5, 6, 2, 10, 15, 3, 20 , 1, 4]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else: 
        return False

xyz = (i for i in input_list if div_by_five(i))

# this is pretty much what the expression above does except values are not being stored
# xyz = []
# for i in input_list:
#     if div_by_five:
#         xyz.append(i)

##for i in xyz:
##    print(i)

## this is the same as above
# [print(i) for i in xyz]


xyz = [i for i in input_list if div_by_five(i)]
# print(xyz)
# 
# [print(i) for i in xyz]
# 
# list((print(i) for i in xyz)) #no need to do this


# embedded list comprhensions
##[[print(i, ii) for ii in range(5)] for i in range(5)]

#this would be the same as the list comprehensions before
## for i in range(5):
##     for ii in range(5):
##         print(i, ii)

## this would be a way to store all values in an array of tuples
# xyz = [[(i, ii) for ii in range(5)] for i in range(5)]
# print(xyz)


#xyz = ([[i, ii] for ii in range(5)] for i in range(5))
#print([i for i in xyz])


## with generators we can get to start operations without running out of memory
# xyz = (((i, ii) for ii in range(50000)) for i in range(50000))
# for i in xyz:
#     for j in i:
#         print(j) #where j is (i, ii)


## The takeaway is that with list comprehensions you run out of memory
## BUT with generators you run our of time

##Finally a trick:

xyz = (print(i) for i in range(5))

for i in xyz:
    i           ##each i is a print being executed !!
