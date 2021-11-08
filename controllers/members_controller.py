from flask import Blueprint, render_template

from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/members")
def members():
    title = "Members"
    members = member_repository.select_all()
    return render_template("members/index.html", title=title, members=members)