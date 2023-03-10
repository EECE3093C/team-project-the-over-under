# Mar 08 Meeting Notes

Series: Weekly Project Meeting

## Progress Reports

### Ben

- UI mockup approved by the group. However, highlighting moneylines based on positive/negative returns isn't necessary.
- Remote database established in bit.io, and there is a service account capable of connecting to it. If others want access to the web version they'll need to create personal accounts.
- Begun work on querying the database from Python, but lack of established classes (as in OOP classes) is a bottleneck.

There was a question about how errored queries will be handled. In response, the current design destroys/rebuilds the moneylines table at certain intervals. So, any
query that causes a corruption will be shortly overwritten. Additionally, almost all writing actions are for inserting rows, if one is errored it will be easy to remove
the afflicted row.

### Blair

- Created the moneyline class diagram. However, it conflicts with the database design (more on that later).

### Sunny

- Confused about what issue writing templates should entail. We decided on using open source repos as a reference.

### Josh Mckettrick

- Plans to work on integrating Docker over spring break.
- Got the Electron app into the front-end repo, after some trouble. There is a Node.js module that wouldn't fit. Rather than including it, we'll have to run a download ourselves.

### Josh Dickens

- Has been researching crontab with a view to getting the webscrapers to run on a schedule.
- Now that the UI mockup has been created he'll work on HTML scaffolding.

## Open Discussion

### Handling the Extension

After spring break, we'll plan/conduct a "mini sprint" that spans the extra week of iteration 3. It will include new issues in relation to those we've been attacking.

### Database

First, we talked about how the moneylines class should be structured. It was decided that it will hold a pandas database that our main, remote database can draw from.
Also, it was pointed out that the current database design may not be friendly to the mockup UI. To remedy this, it will be redesigned and recreated as part of
iteration 3.
