import requests
from FotMob.Transformation import process_matches, process_standings, process_teams

def fetch_data(season):
    params = {
        'id': 55,
        'season': season
    }
    response = requests.get('https://www.fotmob.com/api/leagues', params=params)
    data = response.json()
    matches = data['matches']['allMatches']
    standings = data['table'][0]['data']['table']['all']

    return matches, standings


def fetch_and_process_data(**kwargs):
    seasons = ["2023/2024", "2022/2023", "2021/2022", "2020/2021"]
    all_matches_data = []
    all_standings_data = []
    all_teams_data=[]

    for season in seasons:
        matches, standings = fetch_data(season)
        all_matches_data.extend(process_matches(matches, season))
        all_standings_data.extend(process_standings(standings, season))
        all_teams_data.extend(process_teams(standings))

    kwargs['ti'].xcom_push(key='matches_data', value=all_matches_data)
    kwargs['ti'].xcom_push(key='standings_data', value=all_standings_data)
    kwargs['ti'].xcom_push(key='teams_data', value=all_teams_data)