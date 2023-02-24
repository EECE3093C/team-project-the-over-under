```mermaid

erDiagram
  sportsbooks ||--|{ moneylines : offer
  sportsbooks {
    string sportsbook PK
    string url
  }
  
  moneylines {
    int moneyline PK
    int odds
    string contestant FK
    string sportsbook FK
  }
  
  competitions ||--|{ contestants : host
  competitions {
    string competition PK
  }
  
  contestants ||--o{ moneylines : cause
  contestants {
    string contestant PK
    string form
    string opponent
    string competition FK
  }

```
