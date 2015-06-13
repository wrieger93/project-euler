(*
    This should be self-explanatory.

    Output: -59231
*)

quadLength[a_, b_] := Length[NestWhileList[# + 1 &, 0, PrimeQ[#^2 + a # + b] &]] - 1;
Print[
    First[Times @@@ MaximalBy[
        Flatten[Table[{a, b}, {a, -999, 999}, {b, -999, 999}], 1],
        quadLength @@ # &
    ]]
];
