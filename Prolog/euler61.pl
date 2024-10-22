/*
 Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:
Triangle
 
P_{3,n}=n(n+1)/2
 
1, 3, 6, 10, 15, ...
Square
 
P_{4,n}=n^2
 
1, 4, 9, 16, 25, ...
Pentagonal
 
P_{5,n}=n(3n-1)/2
 
1, 5, 12, 22, 35, ...
Hexagonal
 
P_{6,n}=n(2n-1)
 
1, 6, 15, 28, 45, ...
Heptagonal
 
P_{7,n}=n(5n-3)/2
 
1, 7, 18, 34, 55, ...
Octagonal
 
P_{8,n}=n(3n-2)
 
1, 8, 21, 40, 65, ...
The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.
The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
Each polygonal type: triangle (P_{3,127}=8128), square (P_{4,91}=8281), and pentagonal (P_{5,44}=2882), is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.

 */

/* 
Solution definition:
    sum of...
    
    There is one number of each polygonal numbers from triagonal to octagonal
    
    Each number connects to another number through the last two digits of one 
        number being the same as the last two digits of the other number

    
*/

triangle_number(N, T) :-
    T is N * (N + 1) // 2.

square_number(N, T) :-
    T is N * N.

pentagonal_number(N, T) :-
    T is N * (3 * N - 1) // 2.

hexagonal_number(N, T) :-
    T is N * (2 * N - 1).

heptagonal_number(N, T) :-
    T is N * (5 * N - 3) // 2.

octagonal_number(N, T) :-
    T is N * (3 * N - 2).

is_four_digit(Number) :-
    Number >= 1000,
    Number < 10000.

four_digit_triangle_numbers(TriangleNumbers) :-
    findall(T, (between(1, 200, N), triangle_number(N, T), is_four_digit(T)), TriangleNumbers).

four_digit_square_numbers(SquareNumbers) :-
    findall(S, (between(1, 100, N), square_number(N, S), is_four_digit(S)), SquareNumbers).

four_digit_pentagonal_numbers(PentagonalNumbers) :-
    findall(P, (between(1, 100, N), pentagonal_number(N, P), is_four_digit(P)), PentagonalNumbers).

four_digit_hexagonal_numbers(HexagonalNumbers) :-
    findall(H, (between(1, 100, N), hexagonal_number(N, H), is_four_digit(H)), HexagonalNumbers).

four_digit_heptagonal_numbers(HeptagonalNumbers) :-
    findall(Hp, (between(1, 100, N), heptagonal_number(N, Hp), is_four_digit(Hp)), HeptagonalNumbers).

four_digit_octagonal_numbers(OctagonalNumbers) :-
    findall(O, (between(1, 100, N), octagonal_number(N, O), is_four_digit(O)), OctagonalNumbers).

linked(A, B) :-
    A_last_two is A mod 100,
    B_first_two is B // 100,
    A_last_two =:= B_first_two.


find_cyclical_figurate_set(CyclicSet) :-
    four_digit_triangle_numbers(TriangleNumbers),
    four_digit_square_numbers(SquareNumbers),
    four_digit_pentagonal_numbers(PentagonalNumbers),
    four_digit_hexagonal_numbers(HexagonalNumbers),
    four_digit_heptagonal_numbers(HeptagonalNumbers),
    four_digit_octagonal_numbers(OctagonalNumbers),

    PolygonalLists = [TriangleNumbers, SquareNumbers, PentagonalNumbers, HexagonalNumbers, HeptagonalNumbers, OctagonalNumbers],
    select_member(A, PolygonalLists, Remaining1),
    select_member(B, Remaining1, Remaining2),
    linked(A, B),
    select_member(C, Remaining2, Remaining3),
    linked(B, C),
    select_member(D, Remaining3, Remaining4),
    linked(C, D),
    select_member(E, Remaining4, Remaining5),
    linked(D, E),
    select_member(F, Remaining5, _),
    linked(E, F),
    linked(F, A),

    % select_member(A, PolygonalLists, Remaining1),
    % select_member(B, Remaining1, Remaining2),
    % select_member(C, Remaining2, Remaining3),
    % select_member(D, Remaining3, Remaining4),
    % select_member(E, Remaining4, Remaining5),
    % select_member(F, Remaining5, _),
    % linked(A, B),
    % linked(B, C),
    % linked(C, D),
    % linked(D, E),
    % linked(E, F),
    % linked(F, A),

    CyclicSet = [A, B, C, D, E, F].


select_member(Member, [Numbers | Rest], Rest) :-
    member(Member, Numbers).
select_member(Member, [Numbers | Rest], [Numbers | Remaining]) :-
    select_member(Member, Rest, Remaining).

sum_list([], 0).
sum_list([Head|Tail], Sum) :-
    sum_list(Tail, TailSum),
    Sum is Head + TailSum.

sum_cyclic_set(Sum) :-
    find_cyclical_figurate_set(CyclicSet),
    sum_list(CyclicSet, Sum).   
