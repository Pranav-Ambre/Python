def repeat(n):
    def decorator(fun):
        def wrapper(a):
            for i in range(n):
                fun(a)
        return wrapper
    return decorator

@repeat(7)

def show(a):
    print(f"Hello {a}")

show("Pranav")