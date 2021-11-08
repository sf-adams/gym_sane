from db.run_sql import run_sql
from models.attendance import Attendance
from models.member import Member
import repositories.member_repository as member_repository
from models.session import Session
import repositories.session_repository as session_repository

def save(attendance):
    sql = "INSERT INTO attendances (member_id, session_id) VALUES (%s, %s) RETURNING id"
    values = [attendance.member.id], [attendance.session.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    attendance.id = id