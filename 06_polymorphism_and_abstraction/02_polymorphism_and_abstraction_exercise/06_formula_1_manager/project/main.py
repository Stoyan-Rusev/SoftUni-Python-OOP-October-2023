# from project.formula_teams.mercedes_team import MercedesTeam
# from project.formula_teams.red_bull_team import RedBullTeam
#
#
# mercedes_team = MercedesTeam(1_000_000)
# red_bull_team = RedBullTeam(2_000_000)
#
# print(mercedes_team.budget)
# mercedes_team.calculate_revenue_after_race(1)
# print(mercedes_team.budget)

from project.f1_season_app import F1SeasonApp

f1_season = F1SeasonApp()

print(f1_season.register_team_for_season("Red Bull", 2000000))
print(f1_season.register_team_for_season("Mercedes", 2500000))
print(f1_season.new_race_results("Nurburgring", 1, 7))
print(f1_season.new_race_results("Silverstone", 10, 1))
