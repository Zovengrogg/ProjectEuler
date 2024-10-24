
threeGon(Answer):-
    
    NumberList = [1, 2, 3, 4, 5, 6],
    select(OuterSmallest, NumberList, Remaining1),
    select(Inner1, Remaining1, Remaining2),
    select(Inner2, Remaining2, Remaining3),
    OuterSmallest + Inner1 + Inner2 =:= 9,
    select(Outer2, Remaining3, Remaining4),
    OuterSmallest < Outer2,
    select(Inner3, Remaining4, Remaining5),
    Outer2 + Inner2 + Inner3 =:= 9,

    select(Outer3, Remaining5, _),
    OuterSmallest < Outer3,
    Outer3 + Inner3 + Inner1 =:= 9,

    Answer is OuterSmallest * 100000000 + Inner1 * 10000000 + Inner2 * 1000000 + Outer2 * 100000 + Inner2 * 10000 + Inner3 * 1000  + Outer3 * 100 + Inner3 * 10 + Inner1.

fiveGon(Answer):-
    
    NumberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    select(OuterSmallest, NumberList, Remaining1),
    select(Inner1, Remaining1, Remaining2),
    select(Inner2, Remaining2, Remaining3),
    Total = OuterSmallest + Inner1 + Inner2,

    select(Outer2, Remaining3, Remaining4),
    OuterSmallest < Outer2,
    select(Inner3, Remaining4, Remaining5),
    Outer2 + Inner2 + Inner3 =:= Total,

    select(Outer3, Remaining5, Remaining6),
    OuterSmallest < Outer3,
    select(Inner4, Remaining6, Remaining7),
    Outer3 + Inner3 + Inner4 =:= Total,
    
    select(Outer4, Remaining7, Remaining8),
    OuterSmallest < Outer4,
    select(Inner5, Remaining8, Remaining9),
    Outer4 + Inner4 + Inner5 =:= Total,
    
    select(Outer5, Remaining9, _),
    OuterSmallest < Outer5,
    Outer5 + Inner5 + Inner1 =:= Total,
    
    List = [OuterSmallest, Inner1, Inner2, Outer2, Inner2, Inner3, Outer3, Inner3, Inner4, Outer4, Inner4, Inner5, Outer5, Inner5, Inner1],

    atomic_list_concat(List, '', Answer).

    