

% Is this just append/3?
conc([], L, L).
conc([X|L1], L2, [X|L3] ) :-
    conc(L1, L2, L3).
    
last(Item, [Item]).
last(Item, [_|Tail]) :-
    last(Item, Tail).

sublist(S, L) :-
    conc(_, L2, L),
    conc(S, _, L2).

even_length([]).
even_length([_,_|Tail]) :-
    even_length(Tail).


odd_length([_]).
odd_length([_,_|Tail]) :-
    odd_length(Tail).

reverse([], []).
reverse([X|Tail], ReversedList) :-
    reverse(Tail, ReversedTail),
    conc(ReversedTail, [X], ReversedList). 

palindrome(List) :-
    reverse(List, List).

shift([X|Tail], Shifted) :-
    append(Tail, [X], Shifted).

means(0, zero). 
means(1, one).
means(2, two).
means(3, three).
means(4, four).
means(5, five).
means(6, six).
means(7, seven).
means(8, eight).
means(9, nine).
means(_, unkown).
translate([], []).
translate([X|Tail], Translated) :-
    means(X, Translate),
    translate(Tail, TranslatedTail),
    append([Translate], TranslatedTail, Translated).

subset([], []).
subset([_|Tail], Subset) :-
    subset(Tail, Subset).

subset([X|Tail], [X|Subset]) :-
    subset(Tail, Subset).

divide_list([], [], []).
divide_list([X|[]], [X], []).
divide_list([X|Tail], L1, L2) :-
    [Y|Tail2] = Tail,
    append([X], List1, L1),
    append([Y], List2, L2),
    divide_list(Tail2, List1, List2).

flatten([], []).
flatten([X|Tail], FlatList) :-
    flatten(X, FlatHead),
    flatten(Tail, FlatTail),
    append(FlatHead, FlatTail, FlatList).

flatten(X, [X]) :-
    atomic(X).
    
% canget() file:///C:/Users/mcharette/Downloads/PROLOG%20PROGRAMMING%20FOR%20ARTIFICIAL%20INTELLIGENCE%20-%20lvan%20Bratko.pdf