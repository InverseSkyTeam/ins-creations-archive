import time

print('单位:ms\n')

t = time.time()
for i in range(1000000): 1 or 0
print('or',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 1 | 0
print('| ',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 0 or 0
print('or',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 0 | 0
print('| ',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 1 or 1
print('or',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 1 | 1
print('| ',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 0 or 1
print('or',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 0 | 1
print('| ',round((time.time()-t)*1000,2))

print()

t = time.time()
for i in range(1000000): 1 and 0
print('and',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 1 & 0
print('&  ',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 0 and 0
print('and',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 0 & 0
print('&  ',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 1 and 1
print('and',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 1 & 1
print('&  ',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 0 and 1
print('and',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 0 & 1
print('&  ',round((time.time()-t)*1000,2))

print()

t = time.time()
for i in range(1000000): 1 != 0
print('!=',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 1 ^ 0
print('^ ',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 0 != 0
print('!=',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 0 ^ 0
print('^ ',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 1 != 1
print('!=',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 1 ^ 1
print('^ ',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 0 != 1
print('!=',round((time.time()-t)*1000,2))

t = time.time()
for i in range(1000000): 0 ^ 1
print('^ ',round((time.time()-t)*1000,2))