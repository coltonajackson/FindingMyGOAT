from classes import League, Team, Player
from time import sleep
import pandas as pd
import os

leagues = []
teams = []
players = []

data_directory = os.path.join(os.getcwd(), "data")


def retrieveLeagues():
    global df
    results = map(lambda x: x, leagues)
    df = pd.DataFrame([item.__dict__ for item in results])


def findLeagueById(query):
    global df
    results = filter(lambda x: str(query) == str(x.id), leagues)
    df = pd.DataFrame([item.__dict__ for item in results])


def findLeagueByName(query):
    global df
    results = filter(lambda x: str(query) in x.name, leagues)
    df = pd.DataFrame([item.__dict__ for item in results])


def findLeagueByCountry(query):
    global df
    results = filter(lambda x: str(query) in x.country, leagues)
    df = pd.DataFrame([item.__dict__ for item in results])


def retrieveTeams():
    global df
    results = map(lambda x: x, teams)
    df = pd.DataFrame([item.__dict__ for item in results])


def findTeamById(query):
    global df
    results = filter(lambda x: str(query) == str(x.id), teams)
    df = pd.DataFrame([item.__dict__ for item in results])


def findTeamByName(query):
    global df
    results = filter(lambda x: str(query) in x.name, teams)
    df = pd.DataFrame([item.__dict__ for item in results])


def findTeamByCountry(query):
    global df
    results = filter(lambda x: str(query) in x.country, teams)
    df = pd.DataFrame([item.__dict__ for item in results])


def findTeamByLeagueId(query):
    global df
    results = filter(lambda x: str(query) == str(x.leagueId), teams)
    df = pd.DataFrame([item.__dict__ for item in results])


def retrievePlayers():
    global df
    results = map(lambda x: x, players)
    df = pd.DataFrame([item.__dict__ for item in results])


def findPlayerById(query):
    global df
    results = filter(lambda x: str(query) == str(x.id), players)
    df = pd.DataFrame([item.__dict__ for item in results])


def findPlayerByFirstName(query):
    global df
    results = filter(lambda x: str(query) in x.firstname, players)
    df = pd.DataFrame([item.__dict__ for item in results])


def findPlayerByLastName(query):
    global df
    results = filter(lambda x: str(query) in x.lastname, players)
    df = pd.DataFrame([item.__dict__ for item in results])


def findPlayerByPosition(query):
    global df
    results = filter(lambda x: str(query) in x.position, players)
    df = pd.DataFrame([item.__dict__ for item in results])


def findPlayerByBirthCountry(query):
    global df
    results = filter(lambda x: str(query) in x.birth_country, players)
    df = pd.DataFrame([item.__dict__ for item in results])


def findPlayerByTeamId(query):
    global df
    results = filter(lambda x: str(query) == str(x.teamId), players)
    df = pd.DataFrame([item.__dict__ for item in results])


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
            retrieveLeagues()
        case "1":
            print("Enter league ID below.")
            query = readInput()
            findLeagueById(query)
        case "2":
            print("Enter league name below.")
            query = readInput()
            findLeagueByName(query)
        case "3":
            print("Enter league country below.")
            query = readInput()
            findLeagueByCountry(query)
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
            retrieveTeams()
        case "1":
            print("Enter team ID below.")
            query = readInput()
            findTeamById(query)
        case "2":
            print("Enter team name below.")
            query = readInput()
            findTeamByName(query)
        case "3":
            print("Enter team country below.")
            query = readInput()
            findTeamByCountry(query)
        case "4":
            print("Enter league ID below.")
            query = readInput()
            findTeamByLeagueId(query)
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
            retrievePlayers()
        case "1":
            print("Enter player ID below.")
            query = readInput()
            findPlayerById(query)
        case "2":
            print("Enter player first name below.")
            query = readInput()
            findPlayerByFirstName(query)
        case "3":
            print("Enter player last name below.")
            query = readInput()
            findPlayerByLastName(query)
        case "4":
            print("Enter player position below.")
            query = readInput()
            findPlayerByPosition(query)
        case "5":
            print("Enter player birth country below.")
            query = readInput()
            findPlayerByBirthCountry(query)
        case "6":
            print("Enter team ID below.")
            query = readInput()
            findPlayerByTeamId(query)
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


def endProgram():
    print(
        "\nThe program has loaded the data. You may access the data by referencing the Pandas DataFrame"
        + "'df' in the iPython console."
    )


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
                print("Sorry we didn't catch the input. Returning to main menu.")

        endProgram()

    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
