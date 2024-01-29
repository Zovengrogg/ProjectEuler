/*
    Project Euler 1
    If we list all the natural numbers below 10 that are multiples of 3 or 5, 
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000
*/


sum_of_3_not_5(0, 0).
sum_of_3_not_5(Ceiling, Result) :-
    Ceiling > 1,
    C1 is Ceiling - 3,
    sum_of_3_not_5(C1, Result1),
    (
        (
            \+ 0 is Ceiling mod 5,
            Result is Ceiling + Result1
        ) ;
        Result is Result1
    ).

sum_of_5(0, 0).
sum_of_5(Ceiling, Result) :-
    Ceiling > 1,
    C1 is Ceiling - 5,
    sum_of_5(C1, Result1),
    Result is Ceiling + Result1.


multiple_of_3_or_5_sum(Ceiling, Result) :-
    Remainder3 is Ceiling mod 3,
    Remainder5 is Ceiling mod 5,
    C1 is Ceiling - Remainder3,
    C2 is Ceiling - Remainder5,
    sum_of_3_not_5(C1, Result1),
    sum_of_5(C2, Result2),
    Result is Result1 + Result2.




