#lang racket
(require rackunit)
(provide prefix?)
(provide sublist?)
(require racket/trace)


; prefix? compares a given prefix to see if it is at the beginning of a given list
(define (prefix? P L)
  (cond [(empty? L) #t]; if at the end of the recursive run on the list or if list is empty, return true
        [(empty? P) #t]; same as previous line, but for the prefix
        [(equal? (first P) (first L)) (prefix? (rest P) (rest L))]; if the first elements of each list match, continue with the rest of the list
        [else #f]; else return false
   )
 )
(trace prefix?)

; sublist?
(define (sublist? S L)
  (cond [(prefix? S L) #t]
        [(false? (member (first S) (rest L))) #f]
        [(equal? (first S) (first (member (first S) (rest L)))) (sublist? (rest S) (rest (member (first S) (rest L))))]
        [else #f]
   )
 )
(trace sublist?)       
        


;provided bool checks
(check-true  (prefix? '()    '(s p a m)))
(check-true  (prefix? '(s p) '(s p a m)))
(check-false (prefix? '(s m) '(s p a m)))
(check-false (prefix? '(p a) '(s p a m)))
(check-true  (sublist? '()    '(s p a m)))
(check-true  (sublist? '(s p) '(s p a m)))
(check-false (sublist? '(s m) '(s p a m)))
(check-true  (sublist? '(p a) '(s p a m)))
  
;additional test cases
(check-true (prefix? '(h)      '(h e l p)))
(check-true (prefix? '(1 2 5)  '(1 2 5 6 7 5 7 4)))
(check-false (prefix? '(h)     '(o h m y)))
(check-false (prefix? '(z z z) '(z z h a j)))
(check-true (sublist? '(6 7 5) '(1 2 5 6 7 5 7 4)))
(check-true (sublist? '(1 2)  '(1 1 1 2 1 1)))
(check-false (sublist? '(2 3 3) '(3 2 2 2 2)))