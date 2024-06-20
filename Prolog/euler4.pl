/*
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 
    2-digit numbers is 9009 = 91 X 99.

    Find the largest palindrome made from the product of two 
    3-digit numbers.
*/

reverse([], []).
reverse([X|Tail], ReversedList) :-
    reverse(Tail, ReversedTail),
    append(ReversedTail, [X], ReversedList). 

palindrome(List) :-
    reverse(List, List).

