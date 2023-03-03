# Node.js Research
## General

Source: [Node.js Introduction](https://www.w3schools.com/nodejs/nodejs_intro.asp)

### Install
[Download Node.js Here](https://nodejs.org)

### Node.js Introduction
Node.js is a free open source server enviornment that uses JavaScript to perform tasks over servers. Common tasks include:
- Opening a file on a server and returning it's content to the client
- Running a script or performing various tasks anytime someone accesses a server or port

Node.js can perform various types of tasks. These include but are not limited too:
- Generating dynamic page content
- Create, open, read, write, delete, and close files on the server
- Collect form data
- Add, delete, or modify data in your database

Node.js files contain tasks that will be executed on certain events, like accessing a port on the server. These files must be initiated on the server.

### Writing and Initiating Node.js Programs

Node.js programs are written in JavaScript and executed using the Command Line Interface. To do this, you will write a program in JavaScript and then access the folder
it was saved in via the Command Line, then type "node "filename".js" to execute it: For example:

```
C:\Users\Name\Folder>node myfile.js
```

### Node.js MySQL

Node.js can be used to modify database applications as noted above. To do this, you need to run the following command in your Command Line to install mysql:

```
C:\Users\Name>npm install mysql
```

In your new JavaScript file, in order to write code related to MySQL, you need to include the following function:

```js
var mysql = require('mysql');
```

Now in the file, you must establish a connection with the MySQL base. Heres an example:
```js
var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "yourusername",
  password: "yourpassword"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});
```
[Connection Code Source](https://www.w3schools.com/nodejs/nodejs_mysql.asp)

Once you are connected, You can query the database to read and write to a MySQL database. This is known as "to query" the database.
The following is an example program for doing so:
```js
con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("Result: " + result);
  });
});
```
[To Query Code Source](https://www.w3schools.com/nodejs/nodejs_mysql.asp)

Once you've done this, you can use SQL syntax to access and modify specific data within the database. For more information on how to use SQL operations,
see the MySQL.md file.
