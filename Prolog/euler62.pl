/*
    The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
        56623104 (384^3) and 66430125 (405^3). 
    In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
    Find the smallest cube for which exactly five permutations of its digits are cube.
*/

% Convert number to list of digits
number_to_digits(Number, Digits) :-
    number_codes(Number, Codes), % Convert number to list of character codes
    maplist(code_to_digit, Codes, Digits). % Convert character codes to digits

% Convert character code to digit
code_to_digit(Code, Digit) :-
    Digit is Code - 48.

% Sort the digits of a number
sort_digits(Number, SortedDigits) :-
    number_to_digits(Number, Digits), % Convert number to list of digits
    msort(Digits, SortedDigits). % Sort the list of digits

% Group numbers by their sorted digit lists
group_by_sorted_digits(Numbers, Grouped) :-
    findall(Sorted-Digit, (member(Number, Numbers), sort_digits(Number, Sorted), Digit = Number), Pairs),
    keysort(Pairs, SortedPairs), % Sort pairs by key
    group_pairs_by_key(SortedPairs, Grouped). % Group pairs by key

% Predicate to generate cubes and group them by sorted digits
generate_cubes(Limit, Dict) :-
    findall(Cube, (between(1, Limit, N), Cube is N^3), Cubes),
    group_by_sorted_digits(Cubes, Dict). % Group pairs by key
    % write(Dict). % Print the dictionary for debugging


find_five_cubes(Dict, Result) :-
    member(_-Cubes, Dict), % We don't care about the sorted value, only the set of Cubes associated with the sorted value
    length(Cubes, 5),
    min_list(Cubes, Result). 

solve_euler62(Result) :-
    Limit = 10000, % Changeable based on needs
    generate_cubes(Limit, Dict),
    find_five_cubes(Dict, Result).
