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