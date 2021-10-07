def display(w,**kwarg): # this is how you define a kwarg with 2* & can use other values as well
    print(kwarg)
    print(w)
    print(type(kwarg))
    print(type(w))
    return None

display('whisky', a="himanshu", b=15, c="IndependenceDay")