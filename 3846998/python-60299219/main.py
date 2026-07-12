# 测试
# print((lambda fn: (lambda f: f(f))(lambda f: fn(lambda x: f(f)(x))))(lambda fac: lambda x: 1 if x == 0 else x * fac(x - 1))(10))
print((lambda fn: (lambda f: f(f))(lambda f: fn(lambda x: f(f)(x))))(lambda qsort: lambda lst: ([] if not lst else (qsort(list(filter(lambda x: x < lst[0], lst))) + [lst[0]] * lst.count(lst[0]) + qsort(list(filter(lambda x: x > lst[0], lst))))))([1, 8, 4, 4, 6, 7, 4, 4, 0, 7, 3, 7, 0, 9, 5, 5, 1, 6, 1, 6]))
