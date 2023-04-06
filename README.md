# FindingMyGOAT

## Instructions to run the project

1. Install required packages to run main.py

```cmd
PS > pip install pandas prettytable
```

2. Run 'main.py' in command prompt or terminal

```cmd
PS > python main.py
```

3. Follow prompts in program to retrieve data as a Pandas DataFrame

```cmd
Loading...

Welcome to Finding My GOAT! Please review the following entries to interact with the program.
Enter '1' for league query
Enter '2' for teams query
Enter '3' for players query
>
```

4. When you complete the request for data, your results will display in a PrettyTable format.

```cmd
Welcome to Finding My GOAT! Please review the following entries to interact with the program.
Enter '1' for leagues query
Enter '2' for teams query
Enter '3' for players query
> 2

Welcome to the Team Menu! Please review the following entries to interact with the program.
Enter '0' to view all teams
Enter '1' for team search by ID
Enter '2' for team search by name
Enter '3' for team search by country
Enter '4' for team search by League ID
> 2
Enter team name below.
> Paris
+----+---------------------+------+---------+----------+
| id |         name        | code | country | leagueId |
+----+---------------------+------+---------+----------+
| 85 | Paris Saint Germain | PAR  |  France |   132    |
+----+---------------------+------+---------+----------+
```
