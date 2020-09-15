#lang racket

(provide superreverse)
(require rackunit)
(require racket/trace)

; superreverse reverses the interior list elements but not the original order of the lists
(define (superreverse L)
  (if (empty? L)
      '(); if list is empty, leave it alone
      (cons (reverse (first L)) (superreverse (rest L))))); add the reverse of the first element of the list to the same of the rest of the list

; duperreverse reverses all interior elements of a list and the entire list itself
(define (duperreverse L)
  (cond [(empty? L) L]; if the list if empty, leave it alone
        [{list? (car L)} (append (duperreverse (cdr L)) (cons (duperreverse (car L)) '()))]; if item of a list is a list reverse it 
        [(append (duperreverse (cdr L)) (list (car L)))]));if not a list, reverse the order
(trace duperreverse); trace for testing/debugging
