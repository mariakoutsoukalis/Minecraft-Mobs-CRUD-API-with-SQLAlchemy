from flask import Flask, request, make_response, jsonify
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Import Database Prototype and Defined Model Architecture(s).
from models import db, Mob

# Establish Correct Path to SQL Database Source.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'mobs.db')}")

# Create Flask Application Instance and Configure with SQLAlchemy.
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False
app.debug = True

# Migrate Database to Most Recent Application Instance.
migrate = Migrate(app, db)

# Reinstantiate Application.
db.init_app(app)

# Script to Test Home GET Request.
# curl -i http://127.0.0.1:<PORT>/
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Minecraft Mobs API!"})

# Script to Test API GET Request.
# curl -i http://127.0.0.1:<PORT>/api
@app.route("/api", methods=["GET"])
def api():
    return jsonify({
        "message": "This API supports access to GET, POST, PATCH, and DELETE requests.",
        "addendum": "This API is powered by Flask-SQLAlchemy for improved database validation."
        })
    
# Script to Test GET Request on All Mob Data.
# curl -i http://127.0.0.1:<PORT>/api/mobs
@app.route("/api/mobs", methods=["GET"])
def get_mobs():
    mobs = Mob.query.all()
    data = [mob.to_dict() for mob in mobs]
    return make_response(jsonify(data), 200)

# Script to Test GET Request on Single Mob Datum.
# curl -i http://127.0.0.1:<PORT>/api/mobs/<int:mob_id>
@app.route("/api/mobs/<int:mob_id>", methods=["GET"])
def get_mob_by_id(mob_id: int):
    mob = Mob.query.filter(Mob.mob_id == mob_id).first()
    if not mob:
        return make_response(jsonify({"error": "Mob not found"}), 404)
    return make_response(jsonify(mob.to_dict()), 200)

# Script to Test POST Request on Mobs.
# curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Ender Dragon","hit_points":100,"damage":8,"speed":5,"is_hostile":true}' http://127.0.0.1:<PORT>/api/mobs
@app.route("/api/mobs", methods=["POST"])
def create_mob():
    try:
        mob = Mob(
            name=request.json["name"],
            hit_points=request.json["hit_points"],
            damage=request.json["damage"],
            speed=request.json["speed"],
            is_hostile=request.json["is_hostile"])
        db.session.add(mob)
        db.session.commit()
        return make_response(jsonify(mob.to_dict()), 200)
    except:
        return make_response(jsonify({"error": "Validation Error"}), 404)

# Script to Test PATCH Request on Single Mob.
# curl -i -H "Content-Type: application/json" -X PATCH -d '{"is_hostile":true}' http://127.0.0.1:<PORT>/api/mobs/<int:mob_id>
@app.route("/api/mobs/<int:mob_id>", methods=["PATCH"])
def update_mob_by_id(mob_id: int):
    mob = Mob.query.filter(Mob.mob_id == mob_id).first()
    if not mob:
        return make_response(jsonify({"error": "Mob not found"}), 404)
    payload = request.json
    try:
        for key in payload:
            setattr(mob, key, payload[key])
        db.session.add(mob)
        db.session.commit()
        return make_response(jsonify(mob.to_dict()), 202)
    except:
        return make_response(jsonify({"error": "Validation Error"}), 404)

# Script to Test DELETE Request on Single Mob.
# curl -H "Content-Type: application/json" -X DELETE http://127.0.0.1:<PORT>/api/mobs/<int:mob_id>
@app.route("/api/mobs/<int:mob_id>", methods=["DELETE"])
def delete_mob_by_id(mob_id: int):
    mob = Mob.query.filter(Mob.mob_id == mob_id).first()
    if not mob:
        return make_response(jsonify({"error": "Mob not found"}), 404)
    db.session.delete(mob)
    db.session.commit()
    return make_response(jsonify(mob.to_dict()), 200)

# Script to Test GET Request on Any Error-Handled Page.
# curl -i http://127.0.0.1:<PORT>/whereami
@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({"error": "Page Not Found!"}), 404)

if __name__ == "__main__":
    app.run(debug=True)