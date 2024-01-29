/*
    Project Euler 2
    Each new term in the Fibonacci sequence is generated 
    by adding the previous two terms. 
    By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose 
    values do not exceed four million, find the sum of the even-valued terms.
*/

even_fib_sum_below(Value, Sum) :-
    even_fib_sum_below(0, 1, Value, 0, Sum).

even_fib_sum_below(_, NextFib, Value, Sum, Sum) :-
    NextFib > Value.

even_fib_sum_below(CurrentFib, NextFib, Value, Acc, Sum) :-
    NextFib =< Value,
    NewAcc is Acc + (NextFib * (1 - NextFib mod 2)),
    NextNextFib is CurrentFib + NextFib,
    even_fib_sum_below(NextFib, NextNextFib, Value, NewAcc, Sum).

