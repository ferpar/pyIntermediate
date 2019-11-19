# @app.route('/contact/')
# def contact():
#     return render_template("contact.html")

def add_wrapping(item):
    def wrapped_item():
        return 'a wrapped up box of {}'.format(str(item()))
    return wrapped_item

@add_wrapping
def new_gpu():
    return 'a new Tesla P100 GPU'

print(new_gpu())


from functools import wraps

def add_wrapping_with_style(style):
    def add_wrapping(item):
        @wraps(item) ## this makes it so that when you ask for __name__ you get the wrapped objects __name__
        def wrapped_item():
            return 'a {} wrapped up box of {}'.format(style, str(item()))
        return wrapped_item
    return add_wrapping


@add_wrapping_with_style('beautifully')
def new_bicycle():
    return 'a new bicycle'

print(new_bicycle())
