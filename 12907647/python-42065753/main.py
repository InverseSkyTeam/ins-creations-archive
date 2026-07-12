import random,copy
class A:
    def __init__(self):
        self.value = random.randint(1,100)
a = A()
a.son = a
a.daughter = copy.deepcopy(a)
print("",
      a.value,
      a.son.value,
      a.son.son.value,
      a.son.son.son.value,
      a == a.son.son.son.son.son,
      "\n",
      a.value,
      a.daughter.value,
      a.son.daughter.value,
      a.daughter.son.value,
      a == a.daughter,
)