import pandas as pd
from itertools import combinations
from Helpers.member import Member
import Helpers.helper_functions as helper
from Helpers.magic_search import magic_search_best_team, magic_search_multiple_teams

path = r"Calculations.xlsx"

df = pd.read_excel(path)

# Get the Id's
Id = df['Id'].tolist()

# Get the drivers and teams
drivers_and_teams = df['Driver'].tolist()
drivers = drivers_and_teams[:20]
teams = drivers_and_teams[20:]

# Get the prices
prices = df['PortugalPrice'].tolist()

# Get the points
total_points = df['Total'].tolist()
race_points = df['PortugalPoints'].tolist()

# Creating the list of objects
members = []

for i in range(30):
    members.append(Member(Id[i], drivers_and_teams[i], prices[i], race_points[i], total_points[i]))

# Creating the combinations
all_combinations = combinations(members, 6)

budget = 101400000

best_team = magic_search_best_team(all_combinations, budget)

helper.print_team(best_team)

# Finding the other best teams
point_threshold = helper.get_race_points(best_team) - 10

all_combinations = combinations(members, 6)

best_teams = magic_search_multiple_teams(all_combinations, budget, point_threshold)

results = []


for i in best_teams:
    row = []
    for j in range(6):
        row.append(i[j].name)
    row.append(helper.price_sum(i))
    row.append(helper.get_race_points(i))
    results.append(row)

df2 = pd.DataFrame(results, columns=['Driver1', 'Driver2', 'Driver3', 'Driver4', 'Driver5', 'Constructor', 'Budget', 'Race Points'])
df2 = df2.sort_values(by=['Race Points'], ascending=False)
pd.set_option('display.width', 200)
#df2 = df2.transpose()
#df2 = df2.melt(['Driver1', 'Driver2'], var_name='Driver3', value_name='Driver4')

df2.to_excel("Results.xlsx", sheet_name='Results', index=False)