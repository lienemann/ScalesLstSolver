# Scales LST solver
A solver for the "shape sudoku" puzzle, a puzzle which is often misused as personality test for job applicants.

The solver will return the first solution which fits the constraints, but can also count the number of solutions.

Caveat: Not all puzzles on the internet (and even during the personality test) have a proper solution for the whole
table; you may encounter puzzles where no solution is found (they can still be solved by hand, but not for the complete
table).

Indices are 0-based, symbols start with 1. A table smaller than size 5 can only use symbols with an index smaller
or equal to that.

See `main.py` for examples.