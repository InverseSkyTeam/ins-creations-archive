(begin
  (define fn (lambda (a)
               (print_i a)
               (newline)
               (if (- a 10)
               (fn (+ a 1))
               0)))
  (fn 1)
  (free_func fn))
