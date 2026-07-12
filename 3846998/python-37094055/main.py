print(
'''
这样的easyl代码
func getsum(a:array[][],l,w)->int
    var sum=0
    for i=0 to l
        for j=0 to w
            assign sum+a[i][j] to sum
        end
    end
    return sum
end
func main()->int
    array[100][100] arr
    var length
    var width
    read length as int
    read width as int
    if length>100
        puts[Length is too large!]
    elif width>100
        puts[Width is too large!]
    else
        for i=0 to length
            for j=0 to width
                read arr[i][j] as int
            end
        end
        puts[sum=]
        write getsum(arr) as int
    end
    return 0;
end

会编译成这样的伪·汇编
start main
func getsum
    value sum
    push 0
    popv sum
    begin
        value i
        push 0
        popv i
    wcond
        pushv i
        pushv l
        lt
    next
        pushv i
        push 1
        add
        popv i
    while
        begin
            value j
            push 0
            popv j
        wcond
            pushv j
            pusv w
            lt
        next
            pushv j
            push 1
            add
            popv j
        while
            pushv sum
            pusharr a
            pushv i
            get
            pushv j
            get
            add
            popv sum
        end
    end
    pushv sum
    ret
func main
    array arr 2 100 100
    value length
    value width
    readint
    popv length
    readint
    popv width
    cond
        pushv length
        push 100
        gt
    if
        puts Length is too large!
    else
        cond
            pushv width
            push 100
            gt
        if
            puts Width is too large!
        else
            begin
                value i
                push 0
                popv i
            wcond
                pushv i
                pushv length
                lt
            next
                pushv i
                push 1
                add
                popv i
            while
                begin
                    value j
                    push 0
                    popv j
                wcond
                    pushv j
                    pusv w
                    lt
                next
                    pushv j
                    push 1
                    add
                    popv j
                while
                    pusharr arr
                    pushv i
                    get
                    pushv j
                    get
                    readint
                    popaddr
                end
            end
            puts sum=
            args
                array a
                expr
                    pusharr arr
                end
                value l
                expr
                    pushv length
                end
                value w
                expr
                    pushv width
                end
            call getsum
            puti
            pop
        end
    end
    push 0
    ret
'''
)