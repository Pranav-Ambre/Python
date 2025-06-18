def decorator(fun):
    def wrapper():
        print("This execute before the function call")
        fun()
        print("This executes after function call")
    return wrapper
@decorator
def show():
    print("Hello Hii Hyy")

show()
# f=decorator(show)
# f()
