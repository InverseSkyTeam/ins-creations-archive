class Stack:
    def __init__(self):
        self.__array = []

    def push(self, content) -> None:
        self.__array.append(content)

    def size(self) -> int:
        return len(self.__array)

    def top(self) -> int:
        return self.__array[self.size() - 1]

    def pop(self) -> None:
        self.__array.pop(self.size() - 1)

    def empty(self) -> bool:
        if (self.size() <= 0):
            return True
        return False

    def out(self) -> None:
        for i in range(len(self.__array)):
            print(self.__array[i], end=" ")
        print("\n")

# 调用示例
# s = "545*+5/"
# mst = Stack()
# for i in range(len(s)):
#
#     if ord(s[i]) >= ord("0") and ord(s[i]) <= ord("9"):
#         mst.push(ord(s[i]) - ord('0'))
#     else:
#         num2 = mst.top();
#         mst.pop();
#         num1 = mst.top();
#         mst.pop();
#         if s[i] == '+':
#             mst.push(num1 + num2);
#         elif s[i] == '-':
#             mst.push(num1 - num2);
#         elif s[i] == '*':
#             mst.push(num1 * num2);
#         elif s[i] == '/':
#             mst.push(num1 / num2);
# print(mst.top())