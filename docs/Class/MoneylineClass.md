```mermaid

classDiagram

    MoneyLine <|-- PremierLeague

    class MoneyLine
    MoneyLine : +String homeTeam
    MoneyLine : +String awayTeam
    MoneyLine : +int homeWin
    MoneyLine : +int awayWin

    class PremierLeague
    PremierLeague : +int draw

```