(*
    This should be self-explanatory.

    Output: 76576500
*)

n = NestWhile[# + 1 &, 1, Length[Divisors[# (# + 1)/2]] <= 500 &];
Print[
    n (n + 1)/2
];
