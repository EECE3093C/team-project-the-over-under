# Database Rules

The following is a loose interpretation of business rules, typical in database design. Consider it a living account of what our database must support.

### Features

1. Aggregate moneylines and filter by league.
2. Each moneyline is accompanied by the competing teams and offering sportsbook.
3. The listed sportsbook should be linked for ease of access.
4. User can enter a wager and have the return refleced on each moneyline.
5. Clicking on a moneyline will show competitors' recent results and a bet score.

### Implied Objects/Relationships

1. A moneylines table and a leagues table. Both moneylines and leagues can have many teams.
2. A teams table and a sportsbooks table. One sportsbook can have many moneylines.
3. Part of the data kept on sportsbooks is a URL.
4. NA: handled in front-end.
5. Part of the data kept on teams is their recent results.
