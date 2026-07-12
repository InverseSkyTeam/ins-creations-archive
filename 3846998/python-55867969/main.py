from time import sleep

print("""准备好，这是绝对的、设计的、付式的——抽象
""")

sleep(3)

print("""ideas.md如下
# Rusp
Rusp是一种名字混合Rust和Lisp的语言，然而并没有Rust的内存管理机制，也没有Lisp的灵活性
Rusp的语法类似Lisp而语义类似于C，当然不可缺少的是Lisp伟大的宏支持（静态展开，不支持递归）
采用等价类型系统（标记类型系统和结构类型系统的折中设计，目的是方便宏生成类型）
没有自带GC，进而也没有闭包，只有全局作用域和当前作用域
当然，也没有伟大的call/cc
## 最终目标
- 自举，且代码行数是原来的1/2
- 编译到机器码
- 速度和C相同
- 通过宏实现C++/Rust的全部语义（抽象但是这是Lisp）
- 拥有和C++/Rust相当的标准库
- 实现GUI库
- 实现IDE
## Rusp-py
这是Rusp的一个实验版本，先用Python验证可行性
当然必不可少的-编译到字节码
""")

sleep(3)

print("""syntax.txt如下
(defun fac ([num number]) number
  (if (= num 0)
      1
    (* (fac (- num 1)) num)))

(defun main () number
  (define num 10)
  (put-int (fac num))
  (puts)
  0
  )


; macro确实是静态展开且允许运算，但是只允许访问局部变量
(defmacro hello (name)
  ; puts会对传参做类型检查，保证其全部是字符串（(list number)）类型
  ; 好吧只有number，不要紧以后会改的（
  '(puts "Hello, " ,name "!"))

(defun main () number
  (hello "world")
  0
  )


; 结构体定义
(defstruct A [a b number])

(defun main () number
  (define a (A 1 2))
  (print-int (A-a a))
  (puts)
  (print-int (A-b b))
  (puts)
  0
  )


; 好吧抽象的要来了
; 所以目标中我写到可以通过泛型实现C++的语义
; 薄纱全社区！！！全社区第一个实现泛型！！！（
; 编译：你要耗多少资源（
; 关键这些是全部可编译的
(defmacro vec (T)
  '(struct [size max number] [val (list ,T)]))

(defmacro vec-init (T)
  '((vec ,T) 0 8 (malloc 8)))

; 没错一个不支持闭包的语言有匿名函数
; 这个get-attr/set-attr的设计更是抽象到极致
(defmacro vec-push (T)
  '(lambda ([v (vec ,T)] [i ,T]) void
           (when (= (get-attr size v) (get-attr max v))
             (set-attr max v (* 2 (get-attr max v)))
             (set-attr val v (realloc (get-attr val v) (get-attr max v))))
           (set-nth (get-attr val v) (get-attr size v) i)
           (set-attr size v (+ 1 (get-attr size v)))))

(defmacro vec-get (T)
  '(lambda ([v (vec ,T)] [n number]) ,T
           (get-nth (get-attr val v) n)))

(defun main () number
  (define v (vec-init number)) ; vec<number> v
  ((vec-push number) v 1) ; v.push<number>(1)
  ((vec-push number) v 2) ; v.push<number>(2)
  (print-int ((vec-get number) v 0)) ; v[0]
  (puts)
  ; 一定要平安无事啊（
  0
  )

; 说实话很难想象这玩意成为主流语言
""")

