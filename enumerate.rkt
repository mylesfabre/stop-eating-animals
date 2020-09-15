#lang racket
(require rackunit)
(provide enumerate)
(require racket/trace)

;enumerate turns the elements in a given list into sequentially numbered duos where the first element is the number in the list and the second is the original element
(define (enumerate L)
  (cond [(empty? L) '()]; if list is empty, return empty list
        [else (helpEnumerate 0 L)];calls the helper function to do the heavy lifting :)
        ))
(trace enumerate)

;helpEnumerate does all of the work for enumerate; see enumerate description.
(define (helpEnumerate listIndx L)
  (if (empty? L)
      '()
      (cons (list listIndx (first L)) (helpEnumerate (+ 1 listIndx) (rest L)));create a list of a list of elements with the index and wanted list element. add 1 to the new index in the next call until the list is empty
   )
)
(trace helpEnumerate)

;provided tests
(check-equal? (enumerate '(jan feb mar apr)) 
 '((0 jan) (1 feb) (2 mar) (3 apr)))

(check-equal? (enumerate '(0 I II III IV V VI)) 
                         '((0 0) (1 I) (2 II) (3 III) (4 IV) (5 V) (6 VI)))

(check-equal? (enumerate '())  '())


;additional tests
(check-equal? (enumerate '(4 7 2))
              '((0 4) (1 7) (2 2)))

(check-equal? (enumerate '(beep beep 3 6 3))
              '((0 beep) (1 beep) (2 3) (3 6) (4 3)))