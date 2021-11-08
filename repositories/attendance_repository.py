from pdb import set_trace
from db.run_sql import run_sql
from models.attendance import Attendance
from models.member import Member
import repositories.member_repository as member_repository
from models.session import Session
import repositories.session_repository as session_repository

# CREATE
def save(attendance):
    sql = "INSERT INTO attendances (member_id, session_id) VALUES (%s, %s) RETURNING id"
    values = [attendance.member.id], [attendance.session.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    attendance.id = id

# READ
def select_all():
    attendances = []
    sql = "SELECT * FROM attendances"
    results = run_sql(sql)
    for result in results:
        member = member_repository.select(result["member_id"])
        session = session_repository.select(result["session_id"])
        attendance = Attendance(member, session, result["id"])
        attendances.append(attendance)
    return attendances

def select(id):
    sql = "SELECT * FROM attendances WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = member_repository.select(result["member_id"])
    session = session_repository.select(result["session_id"])
    attendance = Attendance(member, session, result["id"])
    return attendance

# UPDATE
def update(attendance):
    sql = "UPDATE attendances SET (member_id, session_id) = (%s, %s) WHERE id = %s"
    values = [attendance.member.id, attendance.session.id, attendance.id]
    run_sql(sql, values)

# DELETE
def delete_all():
    sql = 'DELETE FROM attendances'
    run_sql(sql)

def delete(id):    
    sql = "DELETE FROM attendances WHERE id = %s"
    values = [id]
    run_sql(sql, values)