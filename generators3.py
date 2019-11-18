## this would be an easy way to create a generator expression (out of a range generator actually)
# (i for i in range(5))

##Now we are gonna create a generator differently

# def simple_gen():
#     yield 'Oh'
#     yield 'hello'
#     yield 'there'
# 
# for i in simple_gen():
#     print(i)
# 
# [print(i) for i in simple_gen()]


## Example about breaking a key:

CORRECT_COMBO = (3, 6, 1)

## found_combo = False
## for c1 in range(10):
##     if found_combo:
##         break
##     for c2 in range(10):
##         if found_combo:
##             break
##         for c3 in range(10):
##             if found_combo:
##                 break
##             if (c1, c2, c3) == CORRECT_COMBO:
##                 print('Found the combo: {}'.format((c1, c2, c3)))
##                 found_combo=True
##                 break
##             print(c1,c2,c3)

### Now instead of this we will do the same using a generator

def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBO:
        print('Found the combo: {}'.format((c1,c2,c3)))
        break
    print(c1, c2, c3)

    ## This way we were able to break with a single statement
