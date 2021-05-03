import Helpers.helper_functions as helper

def magic_search_best_team(all_combinations, budget):
    max_points = 0

    for i in list(all_combinations):
            sum = helper.price_sum(i)
            if (sum <= budget):
                if helper.check_teams_number(i):
                    if helper.get_race_points(i) > max_points:
                        max_points = helper.get_race_points(i)
                        best_team = i
    return best_team

def magic_search_multiple_teams(all_combinations, budget, point_threshold):
    best_teams = []

    for i in list(all_combinations):
        sum = helper.price_sum(i)
        if (sum <= budget):
            if helper.check_teams_number(i):
                if helper.get_race_points(i) > point_threshold:
                    helper.print_team(i)
                    best_teams.append(i)
    return best_teams
