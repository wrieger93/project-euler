(*
    This should be self-explanatory.

    Output: 171
*)

Print[
    Count[
        DayName /@ Flatten[Table[{year, month, 1}, {year, 1901, 2000}, {month, 1, 12}], 1],
        Sunday
    ]
];
