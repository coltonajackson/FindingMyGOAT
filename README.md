# FindingMyGOAT

## Instructions to run the project

1. Install required packages to run main.py

```cmd
> pip install pandas ipython
```

2. Run IPython console in command prompt or terminal

```cmd
> ipython
```

3. Execute 'main.py' file inside of IPython console

```cmd
In [1]: exec(open("main.py").read())
```

4. Follow prompts in program to retrieve data as a Pandas DataFrame

```cmd
Loading...

Welcome to Finding My GOAT! Please review the following entries to interact with the program.
Enter '1' for league query
Enter '2' for teams query
Enter '3' for players query
>
```

5. When you complete the request for data, the data will be stored as variable 'df'. Simply call the varialble in IPython console to review results.

```cmd
The program has loaded the data. You may access the data by referencing the Pandas DataFrame 'df' in the IPython console.

In [2]: df
Out[2]:
      id                                   name    country
0    850  UEFA U21 Championship - Qualification      World
1     36  Africa Cup of Nations - Qualification      World
2    886  UEFA U17 Championship - Qualification      World
3    565                       Liga Primera U20  Nicaragua
4    720                               Emir Cup     Kuwait
..   ...                                    ...        ...
234  969                       Primeira Divisão      Macao
235  364                                1. Liga     Latvia
236  282                       Segunda División       Peru
237  936                        Catarinense - 2     Brazil
238  970                         CONMEBOL - U17      World

[239 rows x 3 columns]
```
