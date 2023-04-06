from classes import League, Team, Player
from time import sleep
import pandas as pd
from prettytable import PrettyTable
import os

leagues = []
teams = []
players = []

data_directory = os.path.join(os.getcwd(), "data")


def retrieveLeagues():
    results = map(lambda x: x, leagues)
    table = PrettyTable(["id", "name", "country"])
    for item in results:
        table.add_row([item.id, item.name, item.country])
    return table


def findLeagueById(query):
    results = filter(lambda x: str(query) == str(x.id), leagues)
    table = PrettyTable(["id", "name", "country"])
    for item in results:
        table.add_row([item.id, item.name, item.country])
    return table


def findLeagueByName(query):
    results = filter(lambda x: str(query) in x.name, leagues)
    table = PrettyTable(["id", "name", "country"])
    for item in results:
        table.add_row([item.id, item.name, item.country])
    return table


def findLeagueByCountry(query):
    results = filter(lambda x: str(query) in x.country, leagues)
    table = PrettyTable(["id", "name", "country"])
    for item in results:
        table.add_row([item.id, item.name, item.country])
    return table


def retrieveTeams():
    results = map(lambda x: x, teams)
    table = PrettyTable(["id", "name", "code", "country", "leagueId"])
    for item in results:
        table.add_row([item.id, item.name, item.code, item.country, item.leagueId])
    return table


def findTeamById(query):
    results = filter(lambda x: str(query) == str(x.id), teams)
    table = PrettyTable(["id", "name", "code", "country", "leagueId"])
    for item in results:
        table.add_row([item.id, item.name, item.code, item.country, item.leagueId])
    return table


def findTeamByName(query):
    results = filter(lambda x: str(query) in x.name, teams)
    table = PrettyTable(["id", "name", "code", "country", "leagueId"])
    for item in results:
        table.add_row([item.id, item.name, item.code, item.country, item.leagueId])
    return table


def findTeamByCountry(query):
    results = filter(lambda x: str(query) in x.country, teams)
    table = PrettyTable(["id", "name", "code", "country", "leagueId"])
    for item in results:
        table.add_row([item.id, item.name, item.code, item.country, item.leagueId])
    return table


def findTeamByLeagueId(query):
    results = filter(lambda x: str(query) == str(x.leagueId), teams)
    table = PrettyTable(["id", "name", "code", "country", "leagueId"])
    for item in results:
        table.add_row([item.id, item.name, item.code, item.country, item.leagueId])
    return table


def retrievePlayers():
    results = map(lambda x: x, players)
    table = PrettyTable(
        ["id", "firstname", "lastname", "position", "age", "birth_country", "teamId"]
    )
    for item in results:
        table.add_row(
            [
                item.id,
                item.firstname,
                item.lastname,
                item.position,
                item.age,
                item.birth_country,
                item.teamId,
            ]
        )
    return table


def findPlayerById(query):
    results = filter(lambda x: str(query) == str(x.id), players)
    table = PrettyTable(
        ["id", "firstname", "lastname", "position", "age", "birth_country", "teamId"]
    )
    for item in results:
        table.add_row(
            [
                item.id,
                item.firstname,
                item.lastname,
                item.position,
                item.age,
                item.birth_country,
                item.teamId,
            ]
        )
    return table


def findPlayerByFirstName(query):
    results = filter(lambda x: str(query) in x.firstname, players)
    table = PrettyTable(
        ["id", "firstname", "lastname", "position", "age", "birth_country", "teamId"]
    )
    for item in results:
        table.add_row(
            [
                item.id,
                item.firstname,
                item.lastname,
                item.position,
                item.age,
                item.birth_country,
                item.teamId,
            ]
        )
    return table


def findPlayerByLastName(query):
    results = filter(lambda x: str(query) in x.lastname, players)
    table = PrettyTable(
        ["id", "firstname", "lastname", "position", "age", "birth_country", "teamId"]
    )
    for item in results:
        table.add_row(
            [
                item.id,
                item.firstname,
                item.lastname,
                item.position,
                item.age,
                item.birth_country,
                item.teamId,
            ]
        )
    return table


def findPlayerByPosition(query):
    results = filter(lambda x: str(query) in x.position, players)
    table = PrettyTable(
        ["id", "firstname", "lastname", "position", "age", "birth_country", "teamId"]
    )
    for item in results:
        table.add_row(
            [
                item.id,
                item.firstname,
                item.lastname,
                item.position,
                item.age,
                item.birth_country,
                item.teamId,
            ]
        )
    return table


def findPlayerByBirthCountry(query):
    results = filter(lambda x: str(query) in x.birth_country, players)
    table = PrettyTable(
        ["id", "firstname", "lastname", "position", "age", "birth_country", "teamId"]
    )
    for item in results:
        table.add_row(
            [
                item.id,
                item.firstname,
                item.lastname,
                item.position,
                item.age,
                item.birth_country,
                item.teamId,
            ]
        )
    return table


def findPlayerByTeamId(query):
    results = filter(lambda x: str(query) == str(x.teamId), players)
    table = PrettyTable(
        ["id", "firstname", "lastname", "position", "age", "birth_country", "teamId"]
    )
    for item in results:
        table.add_row(
            [
                item.id,
                item.firstname,
                item.lastname,
                item.position,
                item.age,
                item.birth_country,
                item.teamId,
            ]
        )
    return table


def mainMenu():
    print(
        "\nWelcome to Finding My GOAT! Please review the following entries to interact with the program.\n"
        + "Enter '1' for leagues query\n"
        + "Enter '2' for teams query\n"
        + "Enter '3' for players query"
    )


def readInput():
    print(">", end=" ")
    return input()


def leagueMenu():
    print(
        "\nWelcome to the League Menu! Please review the following entries to interact with the program.\n"
        + "Enter '0' to view all leagues\n"
        + "Enter '1' for league search by ID\n"
        + "Enter '2' for league search by name\n"
        + "Enter '3' for league search by country"
    )
    choice = readInput()
    match choice:
        case "0":
            results = retrieveLeagues()
            print(results)
        case "1":
            print("Enter league ID below.")
            query = readInput()
            results = findLeagueById(query)
            print(results)
        case "2":
            print("Enter league name below.")
            query = readInput()
            results = findLeagueByName(query)
            print(results)
        case "3":
            print("Enter league country below.")
            query = readInput()
            results = findLeagueByCountry(query)
            print(results)
        case _:
            print("Sorry we didn't catch the input.")


def teamMenu():
    print(
        "\nWelcome to the Team Menu! Please review the following entries to interact with the program.\n"
        + "Enter '0' to view all teams\n"
        + "Enter '1' for team search by ID\n"
        + "Enter '2' for team search by name\n"
        + "Enter '3' for team search by country\n"
        + "Enter '4' for team search by League ID"
    )
    choice = readInput()
    match choice:
        case "0":
            results = retrieveTeams()
            print(results)
        case "1":
            print("Enter team ID below.")
            query = readInput()
            results = findTeamById(query)
            print(results)
        case "2":
            print("Enter team name below.")
            query = readInput()
            results = findTeamByName(query)
            print(results)
        case "3":
            print("Enter team country below.")
            query = readInput()
            results = findTeamByCountry(query)
            print(results)
        case "4":
            print("Enter league ID below.")
            query = readInput()
            results = findTeamByLeagueId(query)
            print(results)
        case _:
            print("Sorry we didn't catch the input.")


def playerMenu():
    print(
        "\nWelcome to the Player Menu! Please review the following entries to interact with the program.\n"
        + "Enter '0' to view all players\n"
        + "Enter '1' for player search by ID\n"
        + "Enter '2' for player search by first name\n"
        + "Enter '3' for player search by last name\n"
        + "Enter '4' for player search by position\n"
        + "Enter '5' for player search by birth country\n"
        + "Enter '6' for player search by Team ID"
    )
    choice = readInput()
    match choice:
        case "0":
            results = retrievePlayers()
            print(results)
        case "1":
            print("Enter player ID below.")
            query = readInput()
            results = findPlayerById(query)
            print(results)
        case "2":
            print("Enter player first name below.")
            query = readInput()
            results = findPlayerByFirstName(query)
            print(results)
        case "3":
            print("Enter player last name below.")
            query = readInput()
            results = findPlayerByLastName(query)
            print(results)
        case "4":
            print("Enter player position below.")
            query = readInput()
            results = findPlayerByPosition(query)
            print(results)
        case "5":
            print("Enter player birth country below.")
            query = readInput()
            results = findPlayerByBirthCountry(query)
            print(results)
        case "6":
            print("Enter team ID below.")
            query = readInput()
            results = findPlayerByTeamId(query)
            print(results)
        case _:
            print("Sorry we didn't catch the input.")


def loadLeagues():
    df = pd.read_csv(f"{data_directory}\\leagues.csv", low_memory=False)
    df.dropna(inplace=True)
    dfList = df.values.tolist()
    for item in dfList:
        leagues.append(League(item[0], item[1], item[2]))


def loadTeams():
    df = pd.read_csv(f"{data_directory}\\teams.csv", low_memory=False)
    df.dropna(inplace=True)
    df.leagueId = df.leagueId.astype(int)
    dfList = df.values.tolist()
    for item in dfList:
        teams.append(Team(item[0], item[1], item[2], item[3], item[4]))


def loadPlayers():
    df = pd.read_csv(f"{data_directory}\\players.csv", low_memory=False)
    df.dropna(inplace=True)
    df.age = df.age.astype(int)
    df.teamId = df.teamId.astype(int)
    dfList = df.values.tolist()
    for item in dfList:
        players.append(
            Player(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
        )


def loadProgram():
    print("Loading...")
    sleep(3)
    loadLeagues()
    loadTeams()
    loadPlayers()


def main():
    try:
        loadProgram()

        mainMenu()
        choice = readInput()
        match choice:
            case "1":
                leagueMenu()
            case "2":
                teamMenu()
            case "3":
                playerMenu()
            case _:
                print("Sorry we didn't catch the input.")

    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
