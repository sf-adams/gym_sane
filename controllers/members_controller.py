from flask import Blueprint, render_template, request, redirect

from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/members")
def members():
    title = "Members"
    members = member_repository.select_all()
    return render_template("members/index.html", title=title, members=members)

# NEW
@members_blueprint.route("/members/new")
def new_member():
    title = "New Member"
    return render_template("members/new.html", title=title)

# CREATE
@members_blueprint.route("/members", methods=["POST"])
def create_member():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    age = request.form["age"]
    category = request.form["category"]
    new_member = Member(first_name, last_name, age, category)
    member_repository.save(new_member)
    return redirect("/members")

# EDIT
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    title = "Edit Member"
    member = member_repository.select(id)
    return render_template("/members/edit.html", title=title, member=member)

# UPDATE
@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    age = request.form["age"]
    category = request.form["category"]
    member = Member(first_name, last_name, age, category)
    member_repository.update(member)
    return redirect("/members")

# DELETE
@members_blueprint.route("/members/<id>/delete", methods=['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")