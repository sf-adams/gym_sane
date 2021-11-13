# Gymsane

### *Insane in the membrane, gymsane in the brain.*

---

With the Gymsane web app, you can:
* Create, edit and delete Members
* Create, edit and delete Sessions
* Make a booking by adding Members to a Session

---

## Quick Start

This program uses **Flask** to run the web app locally on your machine. To download flask, use this command:
```terminal
pip3 install flask
```

Before running the program, in your terminal you will have to create the database where your program's data will be stored:
```terminal
createdb gym_sane
psql -d gym_sane -f gym_sane.sql
```

Once flask is installed, as well as the other elements of the tech stack detailed below, enter this command to start running the software:
```terminal
flask run
```

Then on your browser, you'll need to use the following url address to access gymsane:
>localhost:5000

## Tech Stack

* HTML/CSS
* Python
* Flask
* Jinja
* PostgreSQL
* Psycopg2