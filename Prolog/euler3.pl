/*
    Project Euler 3
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?
*/


sieve(N, Primes) :-
    Y is floor(sqrt(N)),
    numlist(2, Y, List),
    sieve(List, Primes).

sieve([], []).
sieve([P|T], [P|Primes]) :-
    filtered(P, T, Filtered),
    sieve(Filtered, Primes).

filtered(_, [], []).
filtered(P, [X|T], [X|Filtered]) :-
    X mod P =\= 0,
    filter(P, T, Filtered).
filter(P, [X|T], Filtered) :-
    X mod P =:= 0,
    filter(P, T, Filtered).


largestPrimeFactor(N, Result) :-
    sieve(N, Primes),
    reverse(Primes, RPrimes),
    largestPrimeFactor(RPrimes, N, Result).

largestPrimeFactor([P|_], N, P) :-
    N mod P =:= 0.
largestPrimeFactor([P|T], N, Result) :-
    N mod P =\= 0,
    largestPrimeFactor(T, N, Result).
