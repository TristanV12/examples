answer :-
  power(2,1000,P),
  sumdigits(P, A),
  writeln(A).

power(X,Y,Z) :-
  Z is X**Y.

sumdigits(X, X) :-
  X<10.

sumdigits(X, Y) :-
  X>=10,
  X1 is X // 10,
  X2 is X mod 10,
  sumdigits(X1, Y1),
  Y is Y1 + X2.