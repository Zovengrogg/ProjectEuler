count_digits(0, 0).

count_digits(Number, Count) :-
    Number \= 0,
    Number1 is Number // 10,
    count_digits(Number1, Count1),
    Count is Count1 + 1.

x_exponent(Number, Exponent, Result) :-
    Result is Number ** Exponent.

is_integer(Number) :-
    Number =:= round(Number).

x_exponent_x_digit(Number, Exponent) :-
    x_exponent(Number, Exponent, Result),
    count_digits(Result, Exponent).

determine_exponent_limit(Number, Exponent, Result) :-
    between(0, 100, Exponent),
    x_exponent_x_digit(Number, Exponent),
    Result = (Number, Exponent).

solve_euler63(Count) :-
    findall((Number, Exponent), (between(1, 9, Number), determine_exponent_limit(Number, Exponent, (Number, Exponent))), Results),
    length(Results, Count),
    write(Results).