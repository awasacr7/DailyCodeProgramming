def cons(a,b):
    def pairs(f):
        return f(a,b)
    return pairs

def car(pair):
    return pair(lambda a, b: a)

def cdr(pair):
    return pair(lambda a, b: b)

print(car(cons(2,3)))