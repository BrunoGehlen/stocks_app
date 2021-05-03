# Stocks App
![Badge](https://img.shields.io/badge/Python-Flask-%237159c1?style=for-the-badge)
## Project Description
<p align="left">🚀Stock market summary app</p>

### Autor
---

 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/59672672?s=400&u=b306d7f41e6169ff9c0f948d385b13476e0d8909&v=4" width="100px;" alt="Developer"/>
 <br />
 <sub><b>Bruno Gehlen</b></sub>

Developed by Bruno Gehlen 👋🏽 Contact me!

[![Linkedin Badge](https://img.shields.io/badge/-BrunoGehlen-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/BrunoGehlen/)](https://www.linkedin.com/in/BrunoGehlen/) 
[![Gmail Badge](https://img.shields.io/badge/-tousepc@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:tousepc@gmail.com)](mailto:tousepc@gmail.com)

## Install

Clone this repository:

```shell
$ git clone git@github.com:BrunoGehlen/stocks_app.git
```

Create and activate virtual enviroment:

```shell
$ python -m  venv venv
$ source venv/bin/activate
```

or:

```shell
$ python -m  venv venv && source venv/bin/activate
```

Install dependencies:

```shell
$ pip install -r requirements.txt
```

## To use

Set your virtual enviroment variables:

```shell
$ DB_URI_DEV={ your database URL here}
FLASK_APP=app:create_app
FLASK_ENV=development >> .env
```

Run:

```shell
$ flask run
```

## Features

- [x] Transaction generator
- [x] Retrieve daily transactions
- [x] Retrieve most relevant companies

### 🛠 Technologies

- [Python](https://python.org/)
- [React](https://pt-br.reactjs.org/)
