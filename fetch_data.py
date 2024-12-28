import cfbd, os
from collections import defaultdict

config = cfbd.Configuration()
config.api_key['Authorization'] = os.getenv('CFBD_API_KEY')
config.api_key_prefix['Authorization'] = 'Bearer'

year = int(input("Year: "))
starting_team = input("Starting team: ")
ending_team = input("Ending team: ")

win_graph = defaultdict(list)

api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration=config))
games = api_instance.get_games(year=year)


for game in games:
    if game.home_points is not None and game.away_points is not None:
        if game.home_points > game.away_points:
            win_graph[game.home_team].append(game.away_team)
        else:
            win_graph[game.away_team].append(game.home_team)

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
    print("The target team had no losses!")
else:
    message = ''
    for team in path[:-1]:
        message += team + " beat "
    message += path[-1]
    print(message)



