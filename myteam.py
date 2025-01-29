import cfbd, os
from collections import defaultdict

config = cfbd.Configuration()
config.api_key['Authorization'] = os.getenv('CFBD_API_KEY')
config.api_key_prefix['Authorization'] = 'Bearer'

year = int(input("Year: "))

win_graph = defaultdict(list)

api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration=config))
games = api_instance.get_games(year=year, season_type='regular') + api_instance.get_games(year=year, season_type='postseason')

for game in games:
    if game.home_points is not None and game.away_points is not None:
        if game.home_points > game.away_points:
            win_graph[game.home_team].append(game.away_team)
        else:
            win_graph[game.away_team].append(game.home_team)

starting_team = input("Starting team: ")
ending_team = input("Ending team: ")

while starting_team not in win_graph or ending_team not in win_graph:
    if starting_team not in win_graph:
        starting_team = input("Invalid team. New starting team: ")
    if ending_team not in win_graph:
        ending_team = input("Invalid team. New end team: ")


queue = []
queue.append((starting_team, [starting_team]))
visited = set()

path = []

while(queue):
    curr = queue.pop(0)
    # queue = queue[1:]
    if str(curr[0]) in visited:
        continue
    visited.add(str(curr[0]))
    if curr[0] == ending_team:
        path = curr[1]
        break
    for neighbor in win_graph[str(curr[0])]:
        if neighbor not in visited:
            queue.append((neighbor, curr[1] + [neighbor]))


if len(path) == 0:
    print("No transitory win path! :(")
else:
    message = ''
    for team in path[:-1]:
        message += team + " beat "
    message += path[-1]
    print(message)



