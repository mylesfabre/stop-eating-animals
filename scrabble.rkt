#lang racket
(require rackunit)
(provide subbag?)
(require racket/trace)

;subbag? evaluates to true if and only if the list B contains all of the elements in S in a quantity at least as large
(define (subbag? S B)
  (cond [(empty? S) #t];if empty, return empty. Or S is finished iterating and subbag? did not return false
        [(false? (member (first S) B)) #f]; checks to see if the first element of S is in B,. if not, it returns false
        [else (subbag? (rest S) (remove (first S) B))]; recurses until it has exhausted S and removes the firsts element of S from B if present
  )
)

; best-word computes the highest-scoring (or "best") Scrabble word, given a particular rack of letters and a list of legal words, WL
(define (best-word rack WL)
  (biggest (organize (if (empty? (allowed rack WL)); takes the maximum of the scored list and returns empty quotes to be scored to zero if empty
                         '("")
                          (allowed rack WL)))))
(trace best-word)

; biggest filters out the largest scored word recursively
(define (biggest duoList)
  (cond [(empty? duoList) '()]
        [(equal? (length duoList) 1) (first duoList)]; if one element, return the element
        [(> (last (first duoList)) (last (first (rest duoList)))) (biggest (cons (first duoList)(rest(rest duoList))))]; if the first score is larger than the second, delete the second and recurse
        [(< (last (first duoList)) (last (first (rest duoList)))) (biggest (rest duoList))]; if the first score is less than the second, recurse with the rest of the list
        [(= (last (first duoList)) (last (first (rest duoList)))) (biggest (cons (first duoList)(rest(rest duoList))))]; if the first score equals the second, delete first recurse with the rest of the list
        ))

; organize organizes the words and scores into the wanted format of '("word" score)
(define (organize ltrs)
  (if (empty? ltrs)
      '()
   (cons (list (first ltrs) (score-word (first ltrs))) (organize (rest ltrs)))))
(trace organize)

;score-word uses score-letter to determine the score for a string and it returns the list of the string and its score
(define (score-word ltrs)
  (if (equal? ltrs "")
      0
      (+ (score-letter (first (string->list ltrs))) (score-word (list->string (rest (string->list ltrs)))))));scores the word recursively, letter by letter, using score-letter

;score-letter determines the score for its arguement
(define (score-letter chrctr)
  (first (rest (assoc chrctr scrabble-tile-bag))));gets the second element off the list that assoc retreived from scrabble-tile-bag
   
;allowed filters the list to only legal words given a rack
(define (allowed rack WL)
  (cond [(empty? WL) '()]
        [(subbag? (string-split (first WL) #rx"(?<=.)(?=.)") (string-split rack #rx"(?<=.)(?=.)")) (cons (first WL) (allowed rack (rest WL)))]; got the split function from stackoverflow
        [else (allowed rack (rest WL))]
  )
)
(trace allowed)

;; scrabble-tile-bag  
;;   letter tile scores and counts from the game of Scrabble
;;   the counts aren't needed. they're obtained from:
;;   http://en.wikipedia.org/wiki/Image:Scrabble_tiles_en.jpg
;;
(define scrabble-tile-bag
  '((#\a 1 9) (#\b 3 2) (#\c 3 2) (#\d 2 4) (#\e 1 12)
   (#\f 4 2) (#\g 2 3) (#\h 4 2) (#\i 1 9) (#\j 8 1)
   (#\k 5 1) (#\l 1 4) (#\m 3 2) (#\n 1 6) (#\o 1 8)
   (#\p 3 2) (#\q 10 1)(#\r 1 6) (#\s 1 4) (#\t 1 6)
   (#\u 1 4) (#\v 4 2) (#\w 4 2) (#\x 8 1) (#\y 4 2)
   (#\z 10 1) (#\_ 0 2)) ) 
;; end define scrabble-tile-bag
;; The underscore will be used to represent a blank tile, which is a wild-card


;provided tests
(check-equal? (subbag? '()      '(s p a m s))   true)
(check-equal? (subbag? '(s s)   '(s p a m s))   true)
(check-equal? (subbag? '(s m)   '(s p a m s))   true)
(check-equal? (subbag? '(a p)   '(s p a m s))   true)
(check-equal? (subbag? '(a m a) '(s p a m s))   false)
(check-equal? (subbag? '(a s)   '(s a))         true)
(check-equal? (best-word "academy" '("ace" "ade" "cad" "cay" "day")) 
 '("cay" 8))
(check-equal? (best-word "appler"  '("peal" "peel" "ape" "paper")) 
 '("paper" 9))
(check-equal? (best-word "paler"   '("peal" "peel" "ape" "paper"))
 '("peal" 6))
(check-equal? (best-word "kwyjibo" '("ace" "ade" "cad" "cay" "day"))
 '("" 0))
(check-equal? (second (best-word "bcademy" '("ace" "ade" "cad" "cay" "bay"))) 8)

;additional tests
(check-equal? (subbag? '()      '())   true)
(check-equal? (subbag? '(6 8 5 8)      '(s 6 s 8 j 8 h 5))   true)