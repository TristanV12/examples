answer(X) :-
  foreach(member(Y, [1,2]), write(Y)),
  number(X, A),
  writeln(A).

ones(X,A) :-
  (X =:= 1 ; X =:= 2 ; X =:= 6),
  A is 3.
ones(X,A) :-
  (X =:= 3 ; X =:= 7 ; X =:= 8),
  A is 5.
ones(X,A) :-
  (X =:= 4 ; X =:= 5 ; X =:= 9),
  A is 4.
ones(X,A) :-
  X =:= 0,
  A is 0.

teens(X,A) :-
  X =:= 10,
  A is 3.
teens(X,A) :-
  (X =:= 11 ; X =:= 12),
  A is 6.
teens(X,A) :-
  (X =:= 13 ; X =:= 14 ; X =:= 18 ; X =:= 19),
  A is 8.
teens(X,A) :-
  (X =:= 15 ; X =:= 16),
  A is 7.
teens(X,A) :-
  X =:= 17,
  A is 9.

tens(X,A) :-
  X < 10,
  ones(X,A).
tens(X,A) :-
  X < 20,
  X > 9,
  teens(X,A).
tens(X,A) :-
  ((X > 19, X < 40) ; (X > 89, X < 100)),
  C is X mod 10,
  ones(C,B),
  A is B + 6.
tens(X,A) :-
  X > 39,
  X < 70,
  C is X mod 10,
  ones(C,B),
  A is B + 5.
tens(X,A) :-
  X > 69,
  X < 80,
  C is X mod 10,
  ones(C,B),
  A is B + 7.

hundreds(X,A) :-
  TP is X mod 100,
  TP =:= 0,
  HP is X // 100,
  ones(HP, B),
  A is B + 7.
hundreds(X,A) :-
  TP is X mod 100,
  TP > 0,
  HP is X // 100,
  ones(HP, B),
  D is B + 10,
  TP is X mod 100,
  tens(TP, C),
  A is D + C.

number(X,A) :-
  X =:= 1000,
  A is 11.
number(X,A) :-
  X > 99,
  hundreds(X,A).
number(X,A) :-
  X < 100,
  tens(X,A). 