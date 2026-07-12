(begin
  (define fac (lambda (a)
                (if (= a 0)
                  1
                  (* (fac (- a 1)) a))))
  (print_i (fac 10))
  (newline)
  (free_func fac))
