(*
    This should be self-explanatory.

    Output: 906609
*)


Print[
    Max @ Select[
        Flatten[Table[a*b, {a, 100, 999}, {b, 100, 999}]],
        IntegerDigits[#] == Reverse[IntegerDigits[#]] &
    ]
];
