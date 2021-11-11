from flask import Blueprint, render_template, request, redirect

from models.booking import Booking
import repositories.booking_repository as booking_repository

from models.session import Session
import repositories.session_repository as session_repository

from models.member import Member
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)

# INDEX
@bookings_blueprint.route("/bookings")
def bookings():
    title = "Bookings"
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", title=title, bookings=bookings)

# SHOW
@bookings_blueprint.route("/bookings/<id>", methods=['GET'])
def show(id):
    member = booking_repository.select(id)
    sessions = booking_repository.sessions(member)
    return render_template("bookings/show.html", member=member, sessions=sessions)

# NEW
@bookings_blueprint.route("/bookings/new")
def new_booking():
    title = "New Booking"
    members = member_repository.select_all()
    sessions = session_repository.select_all()
    return render_template("bookings/new.html", title=title, members=members)

# CREATE
@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    member_id = request.form["member_id"]
    session_id = request.form["session_id"]
    member = member_repository.select(member_id)
    session = session_repository.select(session_id)
    new_booking = Booking(member, session)
    booking_repository.save(new_booking)
    return redirect("/bookings")

# EDIT
@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
    title = "Edit Booking"
    booking = booking_repository.select(id)
    members = member_repository.select_all()
    sessions = session_repository.select_all()
    return render_template("/bookings/edit.html", title=title, booking=booking, members=members, sessions=sessions)

# UPDATE
@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
    member = request.form["member"]
    session = request.form["session"]
    new_booking = Booking(member, session)
    booking_repository.update(new_booking)
    return redirect("/bookings")

# DELETE
@bookings_blueprint.route("/bookings/<id>/delete")
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")