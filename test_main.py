from main import (
    loadLeagues,
    loadTeams,
    loadPlayers,
    leagues,
    teams,
    players,
    findLeagueById,
    findTeamByName,
    findPlayerByBirthCountry,
)
import pytest


def test_findLeagueById():
    loadLeagues()
    id = 128
    lgs = findLeagueById(id)
    for lg in lgs:
        assert filter(lambda x: lg.id == x.id, leagues)


def test_findTeamByName():
    loadTeams()
    name = "Real Madrid"
    tms = findTeamByName(name)
    for tm in tms:
        assert filter(lambda x: tm.id == x.id, teams)


def test_findPlayerByBirthCountry():
    loadPlayers()
    country = "Portugal"
    pls = findPlayerByBirthCountry(country)
    for pl in pls:
        assert filter(lambda x: pl.id in x.id, players)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
