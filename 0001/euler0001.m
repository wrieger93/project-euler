(*
    This should be self-explanatory.

    Output: 233168
*)

Print[
    Total @ Select[
        Range[999],
        Mod[#, 3] == 0 || Mod[#, 5] == 0 &
    ]
];
