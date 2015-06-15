(*
    This should be self-explanatory.

    Output: 31626
*)

dsum[n_] := Total[Divisors[n]] - n;
Print[
    Total[Select[Range[10000], dsum[#] != # && dsum[dsum[#]] == # &]]
];
