import time
def c_card(a):
    h1 = "─"
    h2 = "-"
    f = "!@#$%^&*()_+-=,.`\[]{};':<>|"
    list = [49,50,51,52,53,54,55,56,57,48,183,65]
    i = 1
    l = 65
    y = 0
    n = 0
    for i in range(57):
        if i == 26:
            l=96
        l = l+1
        list.append(l)
    for i in range(len(a)):
        i1 = i+1
        a1 = a[i:i1]
        a1 = ord(a1)
        if a1 in list :
            y = y+1
        else:
            n = n+1
    if n == 0 and y > 0:
        k1 = "─"
        k2 = "-"
    if n > 0 and y == 0:
        k1 = "─"*2
        k2 = "-"*2
    else:
        k1 = "─"
        k2 = "-"
    for i in range(len(a)):
        h1 = h1+k1
        h2 = h2+k2
    if n > 0 and y > 0:
        h1 = h1+"─"*n
        h2 = h2+"-"*n
    print("┌─"+h1+"┐")
    time.sleep(0.05)
    print("│-"+h2+"│")
    time.sleep(0.05)
    print("│ "+a+" │")
    time.sleep(0.05)
    print("│-"+h2+"│")
    time.sleep(0.05)
    print("└─"+h1+"┘")
if __name__ == '__main__':
    c_card("陈锦奕最帅！")