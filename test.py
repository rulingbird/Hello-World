def cs61nay(combiner, n):
    def g(x, i = n):
        if n == 1:
            return x
        def h(y):
            k = combiner(x, y)
            if i-2 >= 1:
                return g(k, i-1)
            else:
                return k
        return h
    return g    

from operator import sub, add, mul

compose = lambda f, g: lambda x: f(g(x))

print(compose(cs61nay(sub, 2), compose(cs61nay(mul, 3)(2),cs61nay(pow, 2)(10))(3))(1)(-21))
