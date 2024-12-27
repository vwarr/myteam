def get_wins_losses(api_instance, team, year):
    games = api_instance.get_games(year=2024, team=team)

    wins = []
    losses = []

    for game in games:
        if game.home_team == team:
            if game.home_points > game.away_points:
                wins.append(game.away_team)
            else:
                losses.append(game.away_team)
        else:
            if game.away_points > game.home_points:
                wins.append(game.home_team)
            else:
                losses.append(game.home_team)

    print(wins, losses)