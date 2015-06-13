(*
    28123 was given in the problem. We subtract the sum of all numbers that
    can be written as the sum of two abundant numbers from the sum of all
    numbers less than the limit.

    Output: 4208058
*)

limit = 28123;
abundants = Select[Range[limit], Total[Divisors[#]] > 2 # &];
Print[
    limit*(limit-1)/2 - Total @ DeleteDuplicates @ Select[
        Plus @@@ Subsets[abundants, {2}],
        # <= 28123 &
    ]
];
