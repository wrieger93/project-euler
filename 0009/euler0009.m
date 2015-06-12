(*
    This should be self-explanatory.

    Output: 31875000
*)

Print[
    Times[a, b, c] /. Solve[{a^2 + b^2 == c^2, 0 < a < b < c, a + b + c == 1000}, {a, b, c}, Integers][[1]]
];
