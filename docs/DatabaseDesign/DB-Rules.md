# Database Rules

The following is a loose interpretation of business rules, typical in database design. Consider it a living account of what our database must support.

### Features

1. Aggregate moneylines and filter by competition.
2. Each moneyline is accompanied by the contestants and offering sportsbook.
3. The listed sportsbook should be linked for ease of access.
4. User can enter a wager and have the return refleced on each moneyline.
5. Clicking on a moneyline will show contestants' recent results and a bet score.

### Implied Objects/Relationships

1. A moneylines table and a competitions table. Competitions have many contestants who have many moneylines.
2. A contestants table and a sportsbooks table. One sportsbook offers many moneylines.
3. Part of the data kept on sportsbooks is a URL.
4. NA: handled in front-end.
5. Part of the data kept on contestants is their recent results.
