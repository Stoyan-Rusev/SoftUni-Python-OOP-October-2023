from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES = 250_000
    SPONSORS = {
                'Oracle': {1: 1_500_000, 2: 800_000},
                'Honda': {8: 20_000, 10: 10_000}
                }

    def __init__(self, budget):
        super().__init__(budget)
