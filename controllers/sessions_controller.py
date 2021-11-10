from flask import Blueprint, render_template, request, redirect

from models.session import Session
import repositories.session_repository as session_repository

from models.member import Member
import repositories.member_repository as member_repository

sessions_blueprint = Blueprint("sessions", __name__)

# INDEX
@sessions_blueprint.route("/sessions")
def sessions():
    title = "Sessions"
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", title=title, sessions=sessions)

# SHOW
@sessions_blueprint.route("/sessions/<id>", methods=['GET'])
def show(id):
    session = session_repository.select(id)
    members = member_repository.sessions(session)
    return render_template("sessions/show.html", session=session, members=members)

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

# EDIT
@sessions_blueprint.route("/sessions/<id>/edit", methods=['GET'])
def edit_session(id):
    title = "Edit Session"
    session = session_repository.select(id)
    return render_template("/sessions/edit.html", title=title, session=session)

# UPDATE
@sessions_blueprint.route("/sessions/<id>", methods=["POST"])
def update_session(id):
    name = request.form["name"]
    time = request.form["time"]
    category = request.form["category"]
    session = Session(name, time, category)
    session_repository.update(session)
    return redirect("/sessions")

# DELETE
@sessions_blueprint.route("/sessions/<id>/delete", methods=['POST'])
def delete_session(id):
    session_repository.delete(id)
    return redirect("/sessions")