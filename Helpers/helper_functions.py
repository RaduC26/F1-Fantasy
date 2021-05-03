def price_sum(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i].price
    return sum

def get_race_points(list):
    count = 0
    td = find_turbo_driver(list)
    if td:
        for i in range(len(list)):
            count += list[i].race_points
        count += list[td].race_points
        return count
    else:
        return 0
    
def get_total_points(list):
    count = 0
    for i in range(len(list)):
        count += list[i].total_points
    return count

def find_turbo_driver(list):
    max = 0
    td = None
    for i in range(len(list)):
        if list[i].price <= 20000000 and list[i].race_points > max and list[i].id <= 20:
            td = i
            max = list[i].race_points
    return td

def check_teams_number(list):
    count = 0
    for i in range(len(list)):
        if list[i].id > 20:
            count += 1
    if count != 1:
        return False
    return True

def print_team(list):
    for i in list:
        print(i.name)
    print("Team budget: " + str(price_sum(list)))
    print("Race points: " + str(get_race_points(list)))
    print("Turbo driver: " + str(list[find_turbo_driver(list)].name))
    print("______________________________")