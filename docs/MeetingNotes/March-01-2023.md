# Meeting Notes

Picking up from week of 02/27, earlier meetings not recorded.

## 03/01

### Bot Detection

We've been having some issues with our webscrapers getting flagged by sportsbooks, mainly FanDuel. It was thought that this could be avoided by having structured
downtime in between runs. So far, that seems to be correct. 15 to 20 runs per day seems feasible, but we'll see.

### Webscraper Generalization + Bug Fix

Josh Dickens got a handful of webscrapers to work from within the same program. So, rather than having one for each, our project will have a general webscraper.
There was also some trouble with webscrapers returning only partial pages. As it turned out, they were taking the HTML before the sportsbooks were finished rendering.
By having our program sleep for ten seconds before pulling HTML, the issue was fixed. The added runtime shouldn't be an issue, since the webscrapers only run in the
backend.

### Parsers

Contrary to webscrapers, the parser programs will be kept separate. It would be possible to connect them, albeit inconsequential.

### Iteration 1 Wrap-up

All pull requests were merged to develop, which was then pushed to main!

### Iteration 2 Planning

Some broad goals...

- Get webscraper running at some time interval that avoids bot detection
- Finish and debug the parsers
- Migrate the database to bit.io and push some webscraped data to it
- Get our repos up-to-standard with file structure, containerization, templated issue writing
- Begin to refactor our code to OOP design
- Begin UI drafting with a mockup and some scaffolding in Electron
