
% Figure 4.1 Structuring information about the family.
family(
    person(tom, fox, date(7, may, 1960), works(bbc, 15200)),
    person(ann, fox, date(9, may, 1961), unemployed),
    [ person(pat, fox, date(5, may, 1983), unemployed),
      person(jim, fox, date(5, may, 1983), unemployed)]).
  
  
child(X) :-
    family(_, _, Children),
    member(X, Children).
  
  
dateofbirth(person(_, _, Date, _), Date).


% Exercise 4.1
% (a) family(person(_, Family, _), _, []).
% (b) child(person(Name, Surname, _, works(_, _))).
% (c) family(person(_, Family, unemployed), person(_, _, works(_, _)), _).


% (d) (Note: doesn't take in mind days, and months)
% family(Husband, Wife, Children),
%   dateofbirth(Husband, date(_, _, HusbandYear)),
%   dateofbirth(Wife, date(_, _, WifeYear)),
%   abs(HusbandYear - WifeYear) >= 15,
%   member(Child, Children).


twins(X, Y) :-
    family(_, _, Children),
    member(X, Children),
    member(Y, Children),
    X \= Y,
    dateofbirth(X, D),
    dateofbirth(Y, D).

nth_member(1, [X|_], X).
nth_member(N, [_|T], X) :-
    N1 is N - 1,
    nth_member(N1, T, X).

final(s3).
trans(s1, a, s1).
trans(s1, a, s2).
trans(s1, b, s1).
trans(s2, b, s3).
trans(s3, b, s4).
silent(s2, s4).
silent(s3, s1).

