from classes import League, Team, Player
from datetime import datetime as dt
from time import sleep
import requests, json, os, csv

API_HOST = "api-football-v1.p.com"
API_KEY = "3710260cf5msh7f73b3c0a04e043p167a68jsnc2b300db4c23"

URL = f"https://{API_HOST}"
HEADERS = {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": API_HOST}

today = dt.now()
current_year = today.year

leagues = []
teams = []
players = []

data_directory = os.path.join(os.getcwd(), "data")


def getLeagues():
    querystring = {"season": current_year}
    response = requests.request(
        "GET", "/".join([URL, "v3", "leagues"]), headers=HEADERS, params=querystring
    )
    data = json.loads(response.text)["response"]
    return data


def getTeamsByLeagueId(id):
    response = requests.request(
        "GET", "/".join([URL, "v2", "teams", "league", str(id)]), headers=HEADERS
    )
    data = json.loads(response.text)["api"]["teams"]
    return data


def getPlayersByTeamId(id):
    response = requests.request(
        "GET", "/".join([URL, "v2", "players", "team", str(id)]), headers=HEADERS
    )
    data = json.loads(response.text)["api"]["players"]
    return data


def getPlayerStats(id):
    querystring = {"id": id, "season": str(current_year)}
    response = requests.request(
        "GET", "/".join([URL, "v3", "players"]), headers=HEADERS, params=querystring
    )
    data = json.loads(response.text)
    return data


def loadLeagues():
    res = getLeagues()
    for item in res:
        league = League(
            item["league"]["id"], item["league"]["name"], item["country"]["name"]
        )
        leagues.append(league)


def loadTeams():
    for league in leagues:
        res = getTeamsByLeagueId(league.id)
        for item in res:
            team = Team(
                item["team_id"], item["name"], item["code"], item["country"], league.id
            )
            teams.append(team)
        sleep(5)


def loadPlayers():
    for team in teams:
        res = getPlayersByTeamId(team.id)
        for item in res:
            player = Player(
                item["player_id"],
                item["firstname"],
                item["lastname"],
                item["position"],
                item["age"],
                item["birth_country"],
                team.id,
            )
            players.append(player)
        sleep(5)


def exportLeaguesToCsv():
    columns = ["id", "name", "country"]
    with open(
        os.path.join(data_directory, "leagues.csv"), "w", newline="", encoding="utf-8"
    ) as leagueCsv:
        writer = csv.writer(leagueCsv)
        writer.writerow(columns)
        for league in leagues:
            writer.writerow([league.id, league.name, league.country])


def exportTeamsToCsv():
    columns = ["id", "name", "code", "country", "leagueId"]
    with open(
        os.path.join(data_directory, "teams.csv"), "w", newline="", encoding="utf-8"
    ) as teamsCsv:
        writer = csv.writer(teamsCsv)
        writer.writerow(columns)
        for team in teams:
            writer.writerow(
                [team.id, team.name, team.code, team.country, team.leagueId]
            )


def exportPlayersToCsv():
    columns = [
        "id",
        "firstname",
        "lastname",
        "position",
        "age",
        "birth_country",
        "teamId",
    ]
    with open(
        os.path.join(data_directory, "players.csv"), "w", newline="", encoding="utf-8"
    ) as playersCsv:
        writer = csv.writer(playersCsv)
        writer.writerow(columns)
        for player in players:
            writer.writerow(
                [
                    player.id,
                    player.firstname,
                    player.lastname,
                    player.position,
                    player.age,
                    player.birth_country,
                    player.teamId,
                ]
            )


def main():
    try:
        loadLeagues()
        loadTeams()
        loadPlayers()
        exportLeaguesToCsv()
        exportTeamsToCsv()
        exportPlayersToCsv()
        print("Export is finished!")

    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
