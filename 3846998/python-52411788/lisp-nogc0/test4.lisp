(begin
  (define print_il
    (lambda (l, len)
      (define i 0)
      (while (< i len)
             (print_i (nth l i))
             (set! i (+ i 1)))
      (newline)))
  (define l (list 1 1 3))
  (print_il l 3)
  (set-nth! l 1 2)
  (print_il l 3)
  (free_func print_il)
  (free l))
