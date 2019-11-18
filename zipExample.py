x = [1, 2, 3, 4]
y = [7, 9, 3, 2]
z = ['a', 'b', 'c', 'd']

## for a,b,c in zip(x, y, z):
##    print(a, b, c)

## print(zip(x,y,z)) #returns a zip object

## for i in zip(x, y, z): 
##    print(i)              #returns tuples with the given values

## Lets convert it to a list
# print(list(zip(x, y, z)))

## With two of its values we can create a dictionary
# print(dict(zip(z, y)))

##Something that one might find:
#[print(a, b, c) for a, b, c in zip(x, y, z)]

# [print(a,b) for a,b in zip(x,y)]
# print(a) ##This a will not be defined, leading to an error

for a,b in zip(x,y):
    print(a,b)

print(a) #But this a has the latest value of a in the for iterator, because the for loop has created variables a and b in the scope it has been created at

## This is dangerous because in the following case the x and y variables with the original lists will be overwritten

for x,y in zip(x,y):
    print(x, y)
print(x) ## original x list has been overwritten

##lessons: 
    ## A) dont use the same variable names in the for iterators as in the input of the operator
    ## B) otherwise use a list comprehension which will only create temporary variables within its own scope
