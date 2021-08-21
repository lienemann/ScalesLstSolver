from ScalesLstSolver import ScalesLstSolver

if __name__ == '__main__':
    solver = ScalesLstSolver(5)
    solver.add_fixed_symbol_from_string_list([
        "-+---",
        "Δ----",
        "-□*OΔ",
        "--□--",
        "----+"
        ])
    #solver.add_fixed_symbol(ScalesLstSolver.NONE, 3, 4)
    solver.print_table(False)
    print("")
    print(solver.solve(4, 4))
    solver.print_table()

    solver.count_solutions = True
    print(solver.solve(0, 1))
    print(solver.number_of_solutions)
