### roughly args and kwargs are list and dictionary arguments for your function.
## For instance:
## def function(asfs, *args=[], **kwargs={})


#blog_1 = 'I am so awesome.'
#blog_2 = 'Cars are cool.'
#blog_3 = 'Aww look at my cat!!'
#
#site_title = 'My Blog'
#
#def blog_posts(title, *args):
#    print(title)
#    for post in args:
#        print(post)
#
#blog_posts(site_title, blog_1, blog_2, blog_3)

##notice how the args parameter allows us to simply stuff in arguments one after the other

#site_title = 'My Blog'
#
#def blog_posts(title, **kwargs):
#    print(title)
#    for p_title, post in kwargs.items():
#        print(p_title, post)
#
#blog_posts(site_title,
#            blog_1 = 'I am so awesome.',
#            blog_2 = 'Cars are cool.',
#            blog_3 = 'Aww look at my cat!!' )


# site_title = 'My Blog'
# 
# def blog_posts(title, *args, **kwargs):
#     print(title)
#     for arg in args:
#         print(arg)
#     for p_title, post in kwargs.items():
#         print(p_title, post)
# 
# blog_posts(site_title,
#             '1', '2', '3',
#             blog_1 = 'I am so awesome.',
#             blog_2 = 'Cars are cool.',
#             blog_3 = 'Aww look at my cat!!' )


### This last part is an example of using *args in an inverse fashion

import matplotlib.pyplot as plt

def graph_operation(x, y):
    print('function that graphs {} and {}'.format(str(x), str(y)))
    plt.plot(x, y)
    plt.show()

x1 = [1, 2, 3]
y1 = [2, 3, 1]

graph_me = [x1,y1]

graph_operation(*graph_me)
