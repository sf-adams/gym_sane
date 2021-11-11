from db.run_sql import run_sql
from models.member import Member
from models.session import Session

# CREATE
def save(member):
    sql = "INSERT INTO members (first_name, last_name, age, category) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.age, member.category]
    results = run_sql(sql, values)
    id = results[0]["id"]
    member.id = id

# READ
def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for result in results:
        member = Member(result["first_name"], result["last_name"], result["age"], result["category"], result["id"])
        members.append(member)
    return members

def select(id):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = Member(result["first_name"], result["last_name"], result["age"], result["category"], result["id"])
    return member

# UPDATE
def update(member):
    sql = "UPDATE members SET (first_name, last_name, age, category) = (%s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.age, member.category, member.id]
    run_sql(sql, values)

# DELETE
def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):    
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# BRIDGE
def sessions(member):
    sessions = []

    sql = "SELECT sessions.* FROM sessions INNER JOIN bookings ON bookings.session_id = sessions.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        session = Session(row['name'], row['time'], row['category'], row['id'])
        sessions.append(session)

    return sessions