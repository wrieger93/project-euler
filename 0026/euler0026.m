(*
    This should be self-explanatory. Look at the docs for RealDigits if confused.

    Output: 983
*)

Print[
    MaximalBy[
        {#[[1]], Length[RealDigits[#[[2]]][[1, 1]]]} & /@ Table[{x, 1/x}, {x, 1, 999}], 
        #[[2]] &
    ][[1, 1]]
];
