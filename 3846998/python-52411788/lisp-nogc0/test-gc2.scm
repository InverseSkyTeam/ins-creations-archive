(begin
  (define l (list 1 2 2))
  (println l)
  (set-nth! l 2 3)
  (println l)
  (println (list-nth l 2))
  (println (list-append l 4))
  (list-append l 5)
  (println l))
