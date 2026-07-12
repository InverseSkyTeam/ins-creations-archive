def interpret(code):
    array = [0]
    p = 0
    i = 0
    c = 0
    print(code)
    while i < len(code):
        if code[i] == '<':
            if p > 0:
                p -= 1
        elif code[i] == '>':
            p += 1
            if len(array) <= p:
                array.append(0)
        elif code[i] == '+':
            array[p] += 1
        elif code[i] == '-':
            if array[p] > 0:
                array[p] -= 1
        elif code[i] == '.':
            print(array[p], chr(array[p]))
        elif code[i] == ',':
            x = input("Input:")
            try:
                y = int(x)
            except ValueError:
                y = ord(x)
            array[p] = y
        elif code[i] == '[':
            if array[p] == 0:
                while code[i] != ']':
                    i += 1
        elif code[i] == ']':
            if array[p] != 0:
                while code[i] != '[':
                    i -= 1
        i += 1
interpret("++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.")