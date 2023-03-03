# Electron Research
This document was created using Electron's Website under Docs. For more information click [here.](https://www.electronjs.org/docs/latest/)
<br>

## Initial Steps
- Install VS Code
- Install Node.js
- [Install git](https://git-scm.com/download/win)

To confirm Node.js was installed type the following in your command terminal:
```console

input: node -v

output: v18.14.2

```

<br>

To confirm git was installed type the following in your command terminal:
```console

input: git --version

output: git version 2.39.2.windows.1

```

<br>

## Capability in our Project
- Chromium and Node.js are embedded into Electron.
  - High use of CPU compared to other application builders.
  - Extremely customizable, but will require additional research.
  - Many popular applications are built on Electron, such as, Slack desktop, WhatsApp desktop, Discord, etc.
<br>

- Build application interface in HTML.
  - What the user sees.
  - Pop-up window.
  - If you have HTML knowledge, you can easily design a page from one folder.
<br>

- Package application code.
  - Node.js API is hosting our application internally.
<br>

- Create distributable folder with application.
  - Executable .app for mac, or .msi for Windows and Linux operating systems.

<br>

## Creating a .json file - Electron Application Project Configuration
Run the following command in your Microsoft Visual Studio Code terminal:
```console

npm init

```
Hit 'enter' for each prompt until you get to entery point. Set entry point as 'main.js' by typing it in and hitting 'enter'.

<br>

Let the terminal run while it creates a package.json file in your Visual Studio Code. To install electron type this command in your terminal:
```console

npm i electron

```
<br>

To confirm electron was installed type the following in your command terminal:
```console

input: electron -v

output: v23.1.0

```
Notice, a package.json file is created in your project. This project now has electron embedded into it
<br>


## Importing Projects into Forge
Forge is a tool in electron designed to help distribute our project. This will create a packaged app to send to users. The benefit is that we can distribute to MAC, Linux, and Windows with the change of a small portion of code.

Terminal Command:
```console

npm install --save-dev @electron-forge/cli
npx electron-forge import

```
<br>

This will add the following to your package.json file:
```.json
 //...
  "scripts": {
    "start": "electron-forge start",
    "package": "electron-forge package",
    "make": "electron-forge make"
  },
  //...
```
<br>

```.json
//...
"devDependencies": {
    "@electron-forge/cli": "^6.0.5",
    "@electron-forge/maker-deb": "^6.0.5",
    "@electron-forge/maker-rpm": "^6.0.5",
    "@electron-forge/maker-squirrel": "^6.0.5",
    "@electron-forge/maker-zip": "^6.0.5",
    "electron": "^23.1.1"
  }
  //...
  ```
  <br>
  
  Now, to crate a distributable project, run the following in the Visual Studio Code terminal:
  ```console
  npm run make
  ```
  <br>
  
This will bundle the app code and package it into a folder. Once the command is complete it will output a folder containing both the distributable folder, and the folder with the packaged application code.

