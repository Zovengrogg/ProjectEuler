/*
    Fib finds the Nth fibonacci number and fib_find finds which term in the sequence a number is if it exists
*/

fib(0, 0).
fib(1, 1).
fib(N, Result) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fib(N1, Result1),
    fib(N2, Result2),
    Result is Result1 + Result2.


fib_find(N, Position) :-
    fib_find(N, 0, Position).

fib_find(N, Pos, Pos) :-
    fib(Pos, N),
    !.

fib_find(N, Pos, Position) :-
    fib(Pos, N1),
    N1 < N,
    Pos1 is Pos + 1,
    fib_find(N, Pos1, Position).

