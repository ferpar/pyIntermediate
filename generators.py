# an example of a generator (range):

# for i in range(5):
#    print(i)

#in python3 this is a generator, this means the values are not being stored in memory

#generators are generally *slower* compared to list comprehensions 
#beacuse their values are dynamically generated instead of stored in memory

#an example of a list comprehension made out of a generator (an array into which we dump the values of the generator)

# xyz = [] 
# for i in range(5):
#     xyz.append(i)
# print(xyz)

#this would be a list comprehension our of a generator
xyz = [i for i in range(5)]
print(xyz)

#whereas this is a generator
xyz = (i for i in range(5))
#you cannot print the contents of a generator unless you first extract them
#  print(list(xyz))
#this list() operation is pretty much iterating over them and appending them to a list
for i in xyz:
    print(i)
##funnily, one you iterate over a generator, it seems to empty itself

zzz = [i for i in range(50000000)]
print(zzz[:5])
zzz = (i for i in range(50000000))
print(list(zzz)[:5])
