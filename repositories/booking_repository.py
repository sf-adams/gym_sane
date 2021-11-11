from pdb import set_trace
from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
import repositories.member_repository as member_repository
from models.session import Session
import repositories.session_repository as session_repository

# CREATE
def save(booking):
    sql = "INSERT INTO bookings (member_id, session_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.session.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id

# READ
def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        member = member_repository.select(result["member_id"])
        session = session_repository.select(result["session_id"])
        booking = Booking(member, session, result["id"])
        bookings.append(booking)
    return bookings

def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = member_repository.select(result["member_id"])
    session = session_repository.select(result["session_id"])
    booking = Booking(member, session, result["id"])
    return booking

# UPDATE
def update(booking):
    sql = "UPDATE bookings SET (member_id, session_id) = (%s, %s) WHERE id = %s"
    values = [booking.member.id, booking.session.id, booking.id]
    run_sql(sql, values)

# DELETE
def delete_all():
    sql = 'DELETE FROM bookings'
    run_sql(sql)

def delete(id):    
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)