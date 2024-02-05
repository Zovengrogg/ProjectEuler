

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
    
:- op( 300, xfx, plays).
:- op( 200, xfy, and).
/*
    Term1 = jimmy plays football and squash
    Term2 = susan plays tennis and basketball and volleyball
*/

plays(jimmy, and(football, squash)).
plays(susan, and(tennis, and(basketball, volleyball))).


:- op(300, xfx, was).
:- op(200, xfy, of).
:- op(100, fx, the).

diana was the secretary of the department.

t(0+1, 1+0).
t(X+0+1, X+1+0).
t(X+1+1, Z) :-
    t(X+1,X1),
    t(X1+1, Z).

:- op(300, xfx, in).
:- op(300, xfx, gives).
:- op(200, fx, [concatenating, deleting]).
:- op(100, xfx, [and, from]).

in(Element, List) :-
    member(Element, List).

gives(concatinating(and(List1,List2)), List3) :-
    conc(List1, List2, List3).

gives(deleting(from(Element, List)), NewList) :-
    delete(Element, List, NewList).

max(X, Y, X) :-
    X >= Y.

max(X, Y, Y) :-
    X < Y.

maxList([X], X).
maxList([X, Y|T], Max) :-
    maxList([Y|T], M),
    max(X, M, Max).

sumList([], 0).
sumList([X|T], Sum) :-
    sumList(T, S),
    Sum is X+S.

% ordered([_]).
% ordered(List) :-
%     reverse(List, [H|T]),
%     maxList([H|T], H),
%     reverse(T, NewList),
%     ordered(NewList).

ordered([]).
ordered([_]).
ordered(X, Y|T) :-
    X =< Y,
    ordered([Y|T]).

subSum([], 0, []).
subSum([_|Tail], Sum, Subset) :-
    subSum(Tail, Sum, Subset).

subSum([X|T], Sum, [X|SubSet]) :-
    subSum(T, S1, SubSet),
    Sum is X + S1.

between(N1, N2, N1) :-
    N1 =< N2.

between(N1, N2, X) :-
     N1 =< N2,
     Next is N1 + 1,
     between(Next, N2, X).


:- op(900, fx, if).
:- op(800, xfy, then).
:- op(700, xfx, else).
:- op(600, xfx, :=).

if X > Y then Z := X else Z := Y.

if(then(X > Y, else(Z := V, Z := _))) :-
    X > Y,
    Z = V.

if(then(X > Y, else(Z := _, Z := V))) :-
    X =< Y,
    Z = V.

/*
    X = 2, Y = 3, Val2 is 2*X, Val4 is 4*X, if Y > Val2 then Z := Y else Z := Val4, if Z > 5 then W := 1 else W := 0.
    X = 2,
    Y = 3,
    Val2 = 4,
    Val4 = Z, Z = 8,
    W = 1
*/

