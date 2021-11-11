from models.booking import Booking
import repositories.booking_repository as booking_repository

from models.session import Session
import repositories.session_repository as session_repository

from models.member import Member
import repositories.member_repository as member_repository

booking_repository.delete_all()
session_repository.delete_all()
member_repository.delete_all()

member_1 = Member("Sam", "Adams", 24, "Strength")
member_repository.save(member_1)

member_2 = Member("Dwayne", "Johnson", 49, "Bodybuilding")
member_repository.save(member_2)

member_3 = Member("Henry", "Caville", 38, "Cardio")
member_repository.save(member_3)

session_1 = Session("No Pain No Gains", "07:00", "Strength")
session_repository.save(session_1)

session_2 = Session("Wishful Shrinking", "07:00", "Cardio")
session_repository.save(session_2)

session_3 = Session("Sun's Out Guns Out", "12:00", "Bodybuilding")
session_repository.save(session_3)

session_4 = Session("Superman Strength", "04:00", "Strength")
session_repository.save(session_4)

booking_1 = Booking(member_1, session_1)
booking_repository.save(booking_1)

booking_2 = Booking(member_2, session_2)
booking_repository.save(booking_2)

booking_3 = Booking(member_3, session_4)
booking_repository.save(booking_3)

booking_4 = Booking(member_1, session_4)
booking_repository.save(booking_4)