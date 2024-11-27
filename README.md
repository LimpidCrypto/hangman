# hangman

## Inhalt
- [hangman](#hangman)
  - [Inhalt](#inhalt)
  - [1. Development](#1-development)
    - [i. Voraussetzungen](#i-voraussetzungen)
    - [ii. Setup](#ii-setup)
      - [Dev Container](#dev-container)
      - [Server Starten](#server-starten)

## 1. Development

### i. Voraussetzungen

1. [VSCode](https://visualstudio.microsoft.com/de/free-developer-offers/)
    1. [Dev Container Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
2. [Docker](https://www.docker.com/products/docker-desktop/)


### ii. Setup

#### Dev Container

1. VSCode öffnen
2. `Strg + Shift + P` und suche nach "Dev Containers: Clone Repository in Container Volume..."
3. Durchnavigieren bis der Repository Name eingegeben werden muss und nach "LimpidCrypto/hangman" suchen
4. Weiter durchnavigieren
5. VSCode setzt den Devcontainer automatisch auf
6. Warten bis Devcontainer komplett konfiguriert wurde

#### Server Starten

1. Führe `cd ./backend && poetry run hangman` in einem Terminal aus, um den Backend Server zu starten.
2. Führe `cd ./frontend && npm start` in einem Terminal aus, um den Frontend Server zu starten.
3. Erreiche das Frontend über [localhost:8080](http://localhost:4200).