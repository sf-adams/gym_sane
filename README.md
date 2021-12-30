<div align="center">
  <a href="https://github.com/sf-adams/gym_sane">
    <img src="static/img/gymsane_favicon.svg" alt="Logo" width="125" height="125">
  </a>
  <h1>Gymsane</h1>

A gym administration app for handling members, sessions and bookings.
<br>
<strong><em>Insane in the membrane, gymsane in the brain.</em></strong>

<!-- <img src = "static/demo_part_one.gif" width ="400" /> <img src = "static/demo_part_two.gif" width ="400" /> -->

[Report Issue](https://github.com/sf-adams/gym_sane/issues)

</div>

## Features
- Create, edit and delete Members
- Create, edit and delete Sessions
- Make a booking by adding Members to a Session

## Tech Stack
- HTML/CSS
- Python
- Flask
- Jinja
- PostgreSQL
- Psycopg2

## Getting Started
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

## Full Brief

A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

### Minimum Viable Product

- The app should allow the gym to create and edit Members
- The app should allow the gym to create and edit Classes
- The app should allow the gym to book members on specific classes
- The app should show a list of all upcoming classes
- The app should show all members that are booked in for a particular class

### Extensions

- Classes could have a maximum capacity, and users can only be added while there is space remaining.
- The gym could be able to give its members Premium or Standard membership. Standard members can only be signed up for classes during off-peak hours.
- The Gym could mark members and classes as active/deactivated. Deactivated members/classes will not appear when creating bookings.