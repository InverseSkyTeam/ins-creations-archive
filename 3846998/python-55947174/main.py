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

print("""syntax.lisp如下
; 没错Rusp语法和语义第二版设计
; 加入一些现代的设计和语法糖

; number自动省略（C版的int也是）
(defun fac (num) number
  (if (= num 0)
    1
    (* (fac (- num 1)) num)))

(defun main () number
  (define num 10)
  ; 内置函数编译由参数类型决定
  (print (fac num) "\n")
  0
  )

; macro确实是静态展开且允许运算，但是只允许访问局部变量和元变量
(defmacro hello (name)
  ; puts会对传参做类型检查，保证其全部是字符串（(list number)）类型
  ; 好吧只有number，不要紧以后会改的（
  '(println "Hello, " ,name "!"))

(defun main () number
  (hello "world")
  0
  )

; 结构体定义
(defstruct A [a b number])

(defun main () number
  (define a (A 1 2))
  ; 更好的属性获取
  (println (a a))
  (println (a b))
  0
  )

; 这里的语法必须大改
; 只有一种逻辑是正确的：宏等参数展开优化，然而更复杂了
; 错误的，所以要使用独立的语法
(deftypegen vec (T)
  [size max number]
  [val (list ,T)]
  ; 方法定义和调用
  :method
  (defun push ([v ,T]) void
      (when (= (self size) (self max))
      ; 这里没办法，Lisp写命令式本来就怪
      (set-attr self max (* 2 (self max)))
      (set-attr self val (realloc (self val) (self max))))
      (set-nth (self val) (self size) v)
      (set-attr self size (+ 1 (self size))))
  (defun get (n) ,T
      (get-nth (self val) n))
  ; 没有RAII怎么行
  :destruct
  (defun *destructor* () void
    (free (self val))
    ())
  )

(defmacro vec-init (T)
  '((vec ,T) 0 8 (malloc 8)))

(defun main () number
  (define v (vec-init number))
  (v push 1)
  (v push 2)
  (println (v get 0))
  0
  )

""")

