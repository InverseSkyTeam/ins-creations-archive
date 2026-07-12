(begin
  (define print_i_nl (lambda (a)
                       (print_i a)
                       (newline)))
  (print_i_nl (* 1 2 3 4 5))
  (print_i_nl (and 0 1))
  (print_i_nl (or 0 1))
  (free_func print_i_nl))
