def process_matches(matches, season):
    all_matches_data = []
    for week in matches:
        match_info = {
            'season': season,
            'round': week['round'],
            'home_team_id': week['home']['id'],
            'away_team_id': week['away']['id'],
            'score': week['status'].get('scoreStr', 'N/A'),
            'time': week['status']['utcTime']
        }
        all_matches_data.append(match_info)
        
    return all_matches_data

def process_standings(standings, season):
    tables_data = []
    for team in standings:
        standing_info = {
            'season': season,
            'rank': team['idx'],
            'team_id': team['id'],
            'played': team['played'],
            'wins': team['wins'],
            'draws': team['draws'],
            'losses': team['losses'],
            'points': team['pts'],
            'scoreStr': team['scoresStr'],
            'goalConDiff': team['goalConDiff']
        }
        tables_data.append(standing_info)
    
    return tables_data

def process_teams(standings):
    tables_data = []
    for team in standings:
        team_info = {
            'team_id': team['id'],
            'team_name': team['name'],
            'short_name': team['shortName']
        }
        tables_data.append(team_info)

    return tables_data