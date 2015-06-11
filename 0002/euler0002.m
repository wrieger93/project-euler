(*
    This should be self-explanatory.

    Output: 4613732
*)

Print[
    Total @ Select[
        Fibonacci /@ Range @ NestWhile[#+1 &, 1, Fibonacci[#] < 4000000 &],
        EvenQ
    ]
];
