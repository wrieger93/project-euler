(*
    Should be self-explanatory. 28123 was given in the problem.

    Output: 4179871
*)

max = 28123;
abundants = Select[Range[max], Total[Divisors[#]] > 2 # &];
Print[
    (max - 1) * max / 2 - Total @ DeleteDuplicates @ Select[
        Flatten @ Table[abundants[[i]]+abundants[[j]], {i,1,Length[abundants]}, {j,i,Length[abundants]}],
        # < max &
    ]
];
