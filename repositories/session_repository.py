from db.run_sql import run_sql
from models.session import Session
from models.member import Member

# CREATE
def save(session):
    sql = "INSERT INTO sessions (name, time, category) VALUES (%s, %s, %s) RETURNING id"
    values = [session.name, session.time, session.category]
    results = run_sql(sql, values)
    id = results[0]['id']
    session.id = id

# READ
def select_all():
    sessions = []
    sql = "SELECT * FROM sessions"
    results = run_sql(sql)
    for result in results:
        session = Session(result["name"], result["time"], result["category"], result["id"])
        sessions.append(session)
    return sessions

def select_all_by_time():
    sessions = []
    sql = "SELECT * FROM sessions ORDER BY time"
    results = run_sql(sql)
    for result in results:
        session = Session(result["name"], result["time"], result["category"], result["id"])
        sessions.append(session)
    return sessions

def select(id):
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    session = Session(result["name"], result["time"], result["category"], result["id"])
    return session

# UPDATE
def update(session):
    sql = "UPDATE sessions SET (name, time, category) = (%s, %s, %s) WHERE id = %s"
    values = [session.name, session.time, session.category, session.id]
    run_sql(sql, values)

# DELETE
def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM sessions where id = %s"
    values = [id]
    run_sql(sql, values)

# BRIDGE
def members(session):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE session_id = %s"
    values = [session.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['age'], row['category'], row['id'])
        members.append(member)

    return members