from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.toy import Toy

toys = Blueprint('toys', 'toys')

# http://127.0.0.1:5000/api/toys
@toys.route('/', methods=["GET"])
def index():
  toys = Toy.query.all()
  return jsonify([toy.serialize() for toy in toys]), 201


# http://127.0.0.1:5000/api/toys/1
@toys.route('/<id>', methods=["GET"])
def show(id):
  toy = Toy.query.filter_by(id=id).first()
  return jsonify(toy.serialize()), 200


# http://127.0.0.1:5000/api/toys/
@toys.route('/', methods=["POST"]) 
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]

  toy = Toy(**data)
  db.session.add(toy)
  db.session.commit()
  return jsonify(toy.serialize()), 201


# http://127.0.0.1:5000/api/toys/1
@toys.route('/<id>', methods=["PUT"]) 
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  toy = Toy.query.filter_by(id=id).first()

  if toy.profile_id != profile["id"]:
    return 'Forbidden', 403

  for key in data:
    setattr(toy, key, data[key])

  db.session.commit()
  return jsonify(toy.serialize()), 200


# http://127.0.0.1:5000/api/toys/1
@toys.route('/<id>', methods=["DELETE"]) 
@login_required
def delete(id):
  profile = read_token(request)
  toy = Toy.query.filter_by(id=id).first()

  if toy.profile_id != profile["id"]:
    return 'Forbidden', 403
    
  db.session.delete(toy)
  db.session.commit()
  return jsonify(message="Success"), 200


@toys.errorhandler(Exception)          
def basic_error(err):
  return jsonify(err=str(err)), 500