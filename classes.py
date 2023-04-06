class League:
    def __init__(self, id, name, country):
        self.id = id
        self.name = name
        self.country = country


class Team:
    def __init__(self, id, name, code, country, leagueId):
        self.id = id
        self.name = name
        self.code = code
        self.country = country
        self.leagueId = leagueId


class Player:
    def __init__(self, id, firstname, lastname, position, age, birth_country, teamId):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.age = age
        self.birth_country = birth_country
        self.teamId = teamId
