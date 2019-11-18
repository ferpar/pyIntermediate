## enumerate returns a tuple with the object and its index

example = ['left', 'right', 'up', 'down']

# for i in range(len(example)): 
#     print(i, example[i])

# this should be better
for i, j in enumerate(example):
    print(i, j)

## first dictionary test
# dict = { "keyA": 32, "keyB": 12 }
# 
# for i, j in enumerate(dict):
#     print(i, j, dict[j])

## this way you can create a dictionary with keys as indexes
new_dict = dict(enumerate(example))
print(new_dict)
