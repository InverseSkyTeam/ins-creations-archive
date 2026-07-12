from rope import Rope

rope = Rope("Hello, World! this is a test to try the multi node feature. this is of the rope data structure")
print(rope)
print("String Count:", len(rope), "\nNode Count:", rope.node_count())
rope.replace("World", "webpy")
print(rope)
print("String Count:", len(rope), "\nNode Count:", rope.node_count())
rope.insert(6, 'Xes')
print(rope)
print("String Count:", len(rope), "\nNode Count:", rope.node_count())
