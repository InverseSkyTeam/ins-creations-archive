from stream import *

print(
    Stream.of(1212, 1231, 23123, 1242, 2421)
    .sort()
    .foreach(print)
    .do(print, "-------------------")
    .filter(lambda a: a > 2420)
    .sort()
    .foreach(print)
    .do(print, "-------------------")
    .find_first(lambda a: a > 1000)
    .or_else("None")
)