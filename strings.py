
names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    #print(f"Hello there! {name}")
    #print("Hello there! " + name)
    #print(' '.join(['Hello there', name]))

    print(', '.join(names))


import os

location_of_files = "./"

file_name = "text"

#print(location_of_files + file_name)    

#with open(os.path.join(location_of_files, file_name)) as f:
#    print(f.read())

#print(open("./text").read())

who = 'Gary'
how_many = 12

#print(who, "bought", how_many, "apples today")
#print('{} bought {} apples today!'.format(who, how_many))

print('{0} bought {1} apples today!'.format(who, how_many))

#print(f"{who} bought {how_many} apples today!")

