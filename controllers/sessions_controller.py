from re import S
from flask import Blueprint, render_template, request, redirect

from models.session import Session
import repositories.session_repository as session_repository

sessions_blueprint = Blueprint("sessions", __name__)

# INDEX
@sessions_blueprint.route("/sessions")
def sessions():
    title = "Sessions"
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", title=title, sessions=sessions)

# NEW
@sessions_blueprint.route("/sessions/new")
def new_session():
    title = "New Session"
    return render_template("sessions/new.html", title=title)

# CREATE
@sessions_blueprint.route("/sessions", methods=["POST"])
def create_session():
    name = request.form["name"]
    time = request.form["time"]
    category = request.form["category"]
    new_session = Session(name, time, category)
    session_repository.save(new_session)
    return redirect("/sessions")

