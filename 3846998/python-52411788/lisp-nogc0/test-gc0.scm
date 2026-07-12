(begin
  (define fac (lambda (a)
                (if (= a 0)
                  1
                  (* (fac (- a 1)) a))))
  (println (fac 10))
  0)
