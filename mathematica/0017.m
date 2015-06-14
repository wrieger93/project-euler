(*
    Mathematica provides a function to convert an integer into its
    English name. Unfortunately it doesn't include "and" like the
    problem asks. There are 99*9 numbers that have "and" so we add
    99*9*3 to the total of the rest of the letters.

    Output:
*)

Print[
    Length @ Flatten[
        StringCases[#, LetterCharacter] & /@ 
        IntegerName[Range[1000], "Words"]
    ] + 99*9*3
];
