# Sprint 2023-02-15: Project Description

## Vision
When designing ***The Over-Under application***, we had to put ourselves in our user’s position. We asked ourselves, what do we have problems with when placing online sports bets? What problems have we grown accustomed to, and how can we improve on them?

The biggest problem we face when betting online, is finding the best **moneyline<sup>1</sup>** odds. With so many different betting websites being created, not all **sportsbooks<sup>2</sup>** can be identical. Thus, there becomes inconsistency where a better could have won more money if they placed the same bet on a different website. We decided to design a feature that will take data from major online sportsbooks, and congregate them into an organized list where you, the user, can see where to place your bet.

We not only aim to improve the accuracy of your bet, but the efficiency. Many sports betters will have several accounts logged in on multiple tabs in their browser and will flip between tabs searching for the information they need. In our application we will not only have options to sort through these databases using filters, but it will also give users instant appraisals once their predetermined budget and bet is selected. This reduces the time spent by the better significantly, as many online websites hold bets in a physical queue in-case you were to place the bet through their site. They clearly need the additional security as their site accepts bets but here, we want to see what the user can win instantly.

Our goal is to help [legal sports gamblers](https://www.americangaming.org/research/state-gaming-map/) and enthusiasts with an issue that large companies are yet to bring to the table. Current options for people now, include purchasing access to sportsbook APIs, to analyze raw data. Our application is much simpler and is designed to pull and organize data, so the application spans from beginner to experienced sports betters. The application will ensure the user makes the most profitable, and safest bet based on real-time data from major sportsbooks. 

**Moneyline<sup>1</sup>**: A bet on which team will win a game.

**Sportsbook<sup>2</sup>**: An establishment that takes bets on sporting events and pays out winnings.


## Software Architecture
Our design is based on a three-part system. The first being collecting data via **webscraping<sup>3</sup>**. Here, we will use an open-source automation tool called [**Selenium IDE**<sup>4</sup>](https://www.selenium.dev/selenium-ide/) in conjunction with Python code. Selenium IDE allows our program to search for different data types and elements based off the HTML code of a website when given a URL. 

From here, we will move that data into an SQL database using [**SQL Socket<sup>5</sup>**](https://sqlsocket.com/) to convert from Python to SQL, where we can temporarily store the data collected from each sportsbook URL. We will begin by collecting match history, moneyline odds, team names, etc. Then our program will take this raw data and neatly organize it based on user inputs.

Finally, we can use SQL Socket again to convert our code back to Python. We do this to send update queries from Python code to a [**Javascript<sup>6</sup>**](https://www.javascript.com/) user interface, where the user will see the data organized in tables. 

**Webscraping<sup>3</sup>**: The process of using bots to extract content and data from a website.

**Selenium IDE<sup>4</sup>**:  A  tool from the *Selenium Test Suite* and can even be used by someone new to developing automated test cases for their web applications.

**SQL Socket<sup>5</sup>**: A program designed for users to input data of different data types into SQL.

**Javascript<sup>6</sup>**: A scripting language that enables you to create dynamically updating content, control multimedia, animate images, any many more.

## Challenges and Risks

